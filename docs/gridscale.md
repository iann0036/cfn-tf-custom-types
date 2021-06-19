# Gridscale Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/gridscale**. The below arguments may be included as the key/value or JSON properties in the secret:

* `source` - (Required) The global source address for the provider you intend to use. In this case, we use `gridscale/gridscale`.
* `version` - (Optional) A version constraint specifying which subset of available provider versions the module is compatible with.
* `uuid` - (Optional) This is the User-UUID for the gridscale API. It can be found [in the panel](https://my.gridscale.io/APIs/).
* `token` - (Optional) This is an API-Token for the gridscale API. It can be created [in the panel](https://my.gridscale.io/APIs/). The created token needs to have full access to be usable by Terraform.
* `api_url` - (Optional) The URL for the API. By default this is set to "https://api.gridscale.io". Do not add a "/" character at the end.
* `http_headers` - (Optional) Custom HTTP headers sent to gridscale API.
* `request_delay_interval` - (Optional) Custom request delay interval in ms. This time interval is used to delay the synchronous request checks, or delay retryable requests. By default this is set to 1000.
* `max_n_retries` - (Optional) Custom maximum number of retries. The retryable requests can be retried up to `max_n_retries`. If `max_n_retries` is reached and the request is not successful, the last error is returned. By default this is set to 1.

## Supported Resources

* [TF::Gridscale::Backupschedule](../resources/gridscale/TF-Gridscale-Backupschedule/docs/README.md)
* [TF::Gridscale::Firewall](../resources/gridscale/TF-Gridscale-Firewall/docs/README.md)
* [TF::Gridscale::Ipv4](../resources/gridscale/TF-Gridscale-Ipv4/docs/README.md)
* [TF::Gridscale::Ipv6](../resources/gridscale/TF-Gridscale-Ipv6/docs/README.md)
* [TF::Gridscale::Isoimage](../resources/gridscale/TF-Gridscale-Isoimage/docs/README.md)
* [TF::Gridscale::K8s](../resources/gridscale/TF-Gridscale-K8s/docs/README.md)
* [TF::Gridscale::Loadbalancer](../resources/gridscale/TF-Gridscale-Loadbalancer/docs/README.md)
* [TF::Gridscale::Mariadb](../resources/gridscale/TF-Gridscale-Mariadb/docs/README.md)
* [TF::Gridscale::MarketplaceApplicationImport](../resources/gridscale/TF-Gridscale-MarketplaceApplicationImport/docs/README.md)
* [TF::Gridscale::MarketplaceApplication](../resources/gridscale/TF-Gridscale-MarketplaceApplication/docs/README.md)
* [TF::Gridscale::Network](../resources/gridscale/TF-Gridscale-Network/docs/README.md)
* [TF::Gridscale::ObjectStorageAccesskey](../resources/gridscale/TF-Gridscale-ObjectStorageAccesskey/docs/README.md)
* [TF::Gridscale::PaasSecurityzone](../resources/gridscale/TF-Gridscale-PaasSecurityzone/docs/README.md)
* [TF::Gridscale::Paas](../resources/gridscale/TF-Gridscale-Paas/docs/README.md)
* [TF::Gridscale::Postgresql](../resources/gridscale/TF-Gridscale-Postgresql/docs/README.md)
* [TF::Gridscale::Server](../resources/gridscale/TF-Gridscale-Server/docs/README.md)
* [TF::Gridscale::Snapshot](../resources/gridscale/TF-Gridscale-Snapshot/docs/README.md)
* [TF::Gridscale::Snapshotschedule](../resources/gridscale/TF-Gridscale-Snapshotschedule/docs/README.md)
* [TF::Gridscale::Sqlserver](../resources/gridscale/TF-Gridscale-Sqlserver/docs/README.md)
* [TF::Gridscale::Sshkey](../resources/gridscale/TF-Gridscale-Sshkey/docs/README.md)
* [TF::Gridscale::SslCertificate](../resources/gridscale/TF-Gridscale-SslCertificate/docs/README.md)
* [TF::Gridscale::StorageClone](../resources/gridscale/TF-Gridscale-StorageClone/docs/README.md)
* [TF::Gridscale::StorageImport](../resources/gridscale/TF-Gridscale-StorageImport/docs/README.md)
* [TF::Gridscale::Storage](../resources/gridscale/TF-Gridscale-Storage/docs/README.md)
* [TF::Gridscale::Template](../resources/gridscale/TF-Gridscale-Template/docs/README.md)