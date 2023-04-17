"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from typing import Any

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_criteo.tap import TapCriteo

SAMPLE_CONFIG: dict[str, Any] = {
    "reports": [
        {
            "name": "daily_metrics",
            "dimensions": [
                "AdvertiserId",
                "AdsetId",
                "CategoryId",
                "Advertiser",
                "Adset",
                "Category",
                "Day",
            ],
            "metrics": [
                "Clicks",
                "Displays",
                "AdvertiserCost",
                "SalesAllClientAttribution",
                "RevenueGeneratedAllClientAttribution",
            ],
        },
    ],
}

# Run standard built-in tap tests from the SDK:
TapCriteoCloud = get_tap_test_class(
    TapCriteo,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(
        max_records_limit=10,
    ),
)
