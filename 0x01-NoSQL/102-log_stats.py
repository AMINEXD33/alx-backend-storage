#!/usr/bin/env python3
"""  Operations with Python using pymongo """
from pymongo import MongoClient


if __name__ == "__main__":
    """this script is trying to get data of some logs"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx

    docs_count = nginx_collection.count_documents({})
    print(f"{docs_count} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    get_and_path_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{get_and_path_count} status check")
    top_ips = nginx_collection.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
            {"$project": {"_id": 0, "ip": "$_id", "count": 1}},
        ]
    )
    print("IPs:")
    for top_ip in top_ips:
        ip = top_ip.get("ip")
        count = top_ip.get("count")
        print(f"\t{ip}: {count}")
