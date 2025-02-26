from unittest.mock import MagicMock, patch

from tests.providers.gcp.gcp_fixtures import (
    GCP_EU1_LOCATION,
    GCP_PROJECT_ID,
    set_mocked_gcp_provider,
)


class Test_logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled:
    def test_no_projects(self):
        logging_client = MagicMock()
        monitoring_client = MagicMock()

        with patch(
            "prowler.providers.common.provider.Provider.get_global_provider",
            return_value=set_mocked_gcp_provider(),
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_client",
            new=logging_client,
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.monitoring_client",
            new=monitoring_client,
        ):
            from prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled import (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled,
            )

            logging_client.metrics = []
            logging_client.project_ids = []
            monitoring_client.alert_policies = []

            check = (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled()
            )
            result = check.execute()
            assert len(result) == 0

    def test_no_log_metric_filters_no_alerts_one_project(self):
        logging_client = MagicMock()
        monitoring_client = MagicMock()

        with patch(
            "prowler.providers.common.provider.Provider.get_global_provider",
            return_value=set_mocked_gcp_provider(),
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_client",
            new=logging_client,
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.monitoring_client",
            new=monitoring_client,
        ):
            from prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled import (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled,
            )

            logging_client.metrics = []
            logging_client.project_ids = [GCP_PROJECT_ID]
            logging_client.region = GCP_EU1_LOCATION

            monitoring_client.alert_policies = []

            check = (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled()
            )
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"There are no log metric filters or alerts associated in project {GCP_PROJECT_ID}."
            )
            assert result[0].resource_id == GCP_PROJECT_ID
            assert result[0].resource_name == ""
            assert result[0].project_id == GCP_PROJECT_ID
            assert result[0].location == GCP_EU1_LOCATION

    def test_log_metric_filters_no_alerts(self):
        logging_client = MagicMock()
        monitoring_client = MagicMock()

        with patch(
            "prowler.providers.common.provider.Provider.get_global_provider",
            return_value=set_mocked_gcp_provider(),
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_client",
            new=logging_client,
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.monitoring_client",
            new=monitoring_client,
        ):
            from prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled import (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled,
            )
            from prowler.providers.gcp.services.logging.logging_service import Metric

            logging_client.metrics = [
                Metric(
                    name="metric_name",
                    type="custom.googleapis.com/invoice/paid/amount",
                    filter='(protoPayload.serviceName="cloudresourcemanager.googleapis.com") AND (ProjectOwnership OR projectOwnerInvitee) OR (protoPayload.serviceData.policyDelta.bindingDeltas.action="REMOVE" AND protoPayload.serviceData.policyDelta.bindingDeltas.role="roles/owner") OR (protoPayload.serviceData.policyDelta.bindingDeltas.action="ADD" AND protoPayload.serviceData.policyDelta.bindingDeltas.role="roles/owner")',
                    project_id=GCP_PROJECT_ID,
                )
            ]
            logging_client.project_ids = [GCP_PROJECT_ID]
            logging_client.region = GCP_EU1_LOCATION

            monitoring_client.alert_policies = []

            check = (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled()
            )
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "FAIL"
            assert (
                result[0].status_extended
                == f"Log metric filter metric_name found but no alerts associated in project {GCP_PROJECT_ID}."
            )
            assert result[0].resource_id == "metric_name"
            assert result[0].resource_name == "metric_name"
            assert result[0].project_id == GCP_PROJECT_ID
            assert result[0].location == GCP_EU1_LOCATION

    def test_log_metric_filters_with_alerts(self):
        logging_client = MagicMock()
        monitoring_client = MagicMock()

        with patch(
            "prowler.providers.common.provider.Provider.get_global_provider",
            return_value=set_mocked_gcp_provider(),
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_client",
            new=logging_client,
        ), patch(
            "prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.monitoring_client",
            new=monitoring_client,
        ):
            from prowler.providers.gcp.services.logging.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled.logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled import (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled,
            )
            from prowler.providers.gcp.services.logging.logging_service import Metric
            from prowler.providers.gcp.services.monitoring.monitoring_service import (
                AlertPolicy,
            )

            logging_client.metrics = [
                Metric(
                    name="metric_name",
                    type="metric_type",
                    filter='(protoPayload.serviceName="cloudresourcemanager.googleapis.com") AND (ProjectOwnership OR projectOwnerInvitee) OR (protoPayload.serviceData.policyDelta.bindingDeltas.action="REMOVE" AND protoPayload.serviceData.policyDelta.bindingDeltas.role="roles/owner") OR (protoPayload.serviceData.policyDelta.bindingDeltas.action="ADD" AND protoPayload.serviceData.policyDelta.bindingDeltas.role="roles/owner")',
                    project_id=GCP_PROJECT_ID,
                )
            ]
            logging_client.project_ids = [GCP_PROJECT_ID]
            logging_client.region = GCP_EU1_LOCATION

            monitoring_client.alert_policies = [
                AlertPolicy(
                    name=f"projects/{GCP_PROJECT_ID}/alertPolicies/alert_policy",
                    display_name="alert_policy",
                    enabled=True,
                    filters=[
                        'metric.type = "logging.googleapis.com/user/metric_name"',
                    ],
                    project_id=GCP_PROJECT_ID,
                )
            ]

            check = (
                logging_log_metric_filter_and_alert_for_project_ownership_changes_enabled()
            )
            result = check.execute()
            assert len(result) == 1
            assert result[0].status == "PASS"
            assert (
                result[0].status_extended
                == f"Log metric filter metric_name found with alert policy alert_policy associated in project {GCP_PROJECT_ID}."
            )
            assert result[0].resource_id == "metric_name"
            assert result[0].resource_name == "metric_name"
            assert result[0].project_id == GCP_PROJECT_ID
            assert result[0].location == GCP_EU1_LOCATION
