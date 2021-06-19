# TF::AVI::Pool

The Pool resource allows the creation and management of Avi Pool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Pool",
    "Properties" : {
        "<a href="#analyticsprofileref" title="AnalyticsProfileRef">AnalyticsProfileRef</a>" : <i>String</i>,
        "<a href="#apicepgname" title="ApicEpgName">ApicEpgName</a>" : <i>String</i>,
        "<a href="#applicationpersistenceprofileref" title="ApplicationPersistenceProfileRef">ApplicationPersistenceProfileRef</a>" : <i>String</i>,
        "<a href="#autoscalelaunchconfigref" title="AutoscaleLaunchConfigRef">AutoscaleLaunchConfigRef</a>" : <i>String</i>,
        "<a href="#autoscalenetworks" title="AutoscaleNetworks">AutoscaleNetworks</a>" : <i>[ String, ... ]</i>,
        "<a href="#autoscalepolicyref" title="AutoscalePolicyRef">AutoscalePolicyRef</a>" : <i>String</i>,
        "<a href="#capacityestimation" title="CapacityEstimation">CapacityEstimation</a>" : <i>Boolean</i>,
        "<a href="#capacityestimationttfbthresh" title="CapacityEstimationTtfbThresh">CapacityEstimationTtfbThresh</a>" : <i>Double</i>,
        "<a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>" : <i>String</i>,
        "<a href="#cloudref" title="CloudRef">CloudRef</a>" : <i>String</i>,
        "<a href="#connectionrampduration" title="ConnectionRampDuration">ConnectionRampDuration</a>" : <i>Double</i>,
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#defaultserverport" title="DefaultServerPort">DefaultServerPort</a>" : <i>Double</i>,
        "<a href="#deleteserverondnsrefresh" title="DeleteServerOnDnsRefresh">DeleteServerOnDnsRefresh</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>[ String, ... ]</i>,
        "<a href="#eastwest" title="EastWest">EastWest</a>" : <i>Boolean</i>,
        "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#externalautoscalegroups" title="ExternalAutoscaleGroups">ExternalAutoscaleGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#fewesttasksfeedbackdelay" title="FewestTasksFeedbackDelay">FewestTasksFeedbackDelay</a>" : <i>Double</i>,
        "<a href="#gracefuldisabletimeout" title="GracefulDisableTimeout">GracefulDisableTimeout</a>" : <i>Double</i>,
        "<a href="#healthmonitorrefs" title="HealthMonitorRefs">HealthMonitorRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#hostcheckenabled" title="HostCheckEnabled">HostCheckEnabled</a>" : <i>Boolean</i>,
        "<a href="#ignoreserverport" title="IgnoreServerPort">IgnoreServerPort</a>" : <i>Boolean</i>,
        "<a href="#ignoreservers" title="IgnoreServers">IgnoreServers</a>" : <i>Boolean</i>,
        "<a href="#inlinehealthmonitor" title="InlineHealthMonitor">InlineHealthMonitor</a>" : <i>Boolean</i>,
        "<a href="#ipaddrgroupref" title="IpaddrgroupRef">IpaddrgroupRef</a>" : <i>String</i>,
        "<a href="#lbalgorithm" title="LbAlgorithm">LbAlgorithm</a>" : <i>String</i>,
        "<a href="#lbalgorithmconsistenthashhdr" title="LbAlgorithmConsistentHashHdr">LbAlgorithmConsistentHashHdr</a>" : <i>String</i>,
        "<a href="#lbalgorithmcorenonaffinity" title="LbAlgorithmCoreNonaffinity">LbAlgorithmCoreNonaffinity</a>" : <i>Double</i>,
        "<a href="#lbalgorithmhash" title="LbAlgorithmHash">LbAlgorithmHash</a>" : <i>String</i>,
        "<a href="#lookupserverbyname" title="LookupServerByName">LookupServerByName</a>" : <i>Boolean</i>,
        "<a href="#maxconcurrentconnectionsperserver" title="MaxConcurrentConnectionsPerServer">MaxConcurrentConnectionsPerServer</a>" : <i>Double</i>,
        "<a href="#minhealthmonitorsup" title="MinHealthMonitorsUp">MinHealthMonitorsUp</a>" : <i>Double</i>,
        "<a href="#minserversup" title="MinServersUp">MinServersUp</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nsxsecuritygroup" title="NsxSecuritygroup">NsxSecuritygroup</a>" : <i>[ String, ... ]</i>,
        "<a href="#pkiprofileref" title="PkiProfileRef">PkiProfileRef</a>" : <i>String</i>,
        "<a href="#requestqueuedepth" title="RequestQueueDepth">RequestQueueDepth</a>" : <i>Double</i>,
        "<a href="#requestqueueenabled" title="RequestQueueEnabled">RequestQueueEnabled</a>" : <i>Boolean</i>,
        "<a href="#resolvepoolbydns" title="ResolvePoolByDns">ResolvePoolByDns</a>" : <i>Boolean</i>,
        "<a href="#rewritehostheadertoservername" title="RewriteHostHeaderToServerName">RewriteHostHeaderToServerName</a>" : <i>Boolean</i>,
        "<a href="#rewritehostheadertosni" title="RewriteHostHeaderToSni">RewriteHostHeaderToSni</a>" : <i>Boolean</i>,
        "<a href="#routingpool" title="RoutingPool">RoutingPool</a>" : <i>Boolean</i>,
        "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
        "<a href="#servertimeout" title="ServerTimeout">ServerTimeout</a>" : <i>Double</i>,
        "<a href="#servicemetadata" title="ServiceMetadata">ServiceMetadata</a>" : <i>String</i>,
        "<a href="#snienabled" title="SniEnabled">SniEnabled</a>" : <i>Boolean</i>,
        "<a href="#sslkeyandcertificateref" title="SslKeyAndCertificateRef">SslKeyAndCertificateRef</a>" : <i>String</i>,
        "<a href="#sslprofileref" title="SslProfileRef">SslProfileRef</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#tier1lr" title="Tier1Lr">Tier1Lr</a>" : <i>String</i>,
        "<a href="#useserviceport" title="UseServicePort">UseServicePort</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vrfref" title="VrfRef">VrfRef</a>" : <i>String</i>,
        "<a href="#analyticspolicy" title="AnalyticsPolicy">AnalyticsPolicy</a>" : <i>[ <a href="analyticspolicydefinition.md">AnalyticsPolicyDefinition</a>, ... ]</i>,
        "<a href="#connpoolproperties" title="ConnPoolProperties">ConnPoolProperties</a>" : <i>[ <a href="connpoolpropertiesdefinition.md">ConnPoolPropertiesDefinition</a>, ... ]</i>,
        "<a href="#failaction" title="FailAction">FailAction</a>" : <i>[ <a href="failactiondefinition.md">FailActionDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#maxconnrateperserver" title="MaxConnRatePerServer">MaxConnRatePerServer</a>" : <i>[ <a href="maxconnrateperserverdefinition.md">MaxConnRatePerServerDefinition</a>, ... ]</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ <a href="networksdefinition.md">NetworksDefinition</a>, ... ]</i>,
        "<a href="#placementnetworks" title="PlacementNetworks">PlacementNetworks</a>" : <i>[ <a href="placementnetworksdefinition.md">PlacementNetworksDefinition</a>, ... ]</i>,
        "<a href="#serverreselect" title="ServerReselect">ServerReselect</a>" : <i>[ <a href="serverreselectdefinition.md">ServerReselectDefinition</a>, ... ]</i>,
        "<a href="#servers" title="Servers">Servers</a>" : <i>[ <a href="serversdefinition.md">ServersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Pool
Properties:
    <a href="#analyticsprofileref" title="AnalyticsProfileRef">AnalyticsProfileRef</a>: <i>String</i>
    <a href="#apicepgname" title="ApicEpgName">ApicEpgName</a>: <i>String</i>
    <a href="#applicationpersistenceprofileref" title="ApplicationPersistenceProfileRef">ApplicationPersistenceProfileRef</a>: <i>String</i>
    <a href="#autoscalelaunchconfigref" title="AutoscaleLaunchConfigRef">AutoscaleLaunchConfigRef</a>: <i>String</i>
    <a href="#autoscalenetworks" title="AutoscaleNetworks">AutoscaleNetworks</a>: <i>
      - String</i>
    <a href="#autoscalepolicyref" title="AutoscalePolicyRef">AutoscalePolicyRef</a>: <i>String</i>
    <a href="#capacityestimation" title="CapacityEstimation">CapacityEstimation</a>: <i>Boolean</i>
    <a href="#capacityestimationttfbthresh" title="CapacityEstimationTtfbThresh">CapacityEstimationTtfbThresh</a>: <i>Double</i>
    <a href="#cloudconfigcksum" title="CloudConfigCksum">CloudConfigCksum</a>: <i>String</i>
    <a href="#cloudref" title="CloudRef">CloudRef</a>: <i>String</i>
    <a href="#connectionrampduration" title="ConnectionRampDuration">ConnectionRampDuration</a>: <i>Double</i>
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#defaultserverport" title="DefaultServerPort">DefaultServerPort</a>: <i>Double</i>
    <a href="#deleteserverondnsrefresh" title="DeleteServerOnDnsRefresh">DeleteServerOnDnsRefresh</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>
      - String</i>
    <a href="#eastwest" title="EastWest">EastWest</a>: <i>Boolean</i>
    <a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#externalautoscalegroups" title="ExternalAutoscaleGroups">ExternalAutoscaleGroups</a>: <i>
      - String</i>
    <a href="#fewesttasksfeedbackdelay" title="FewestTasksFeedbackDelay">FewestTasksFeedbackDelay</a>: <i>Double</i>
    <a href="#gracefuldisabletimeout" title="GracefulDisableTimeout">GracefulDisableTimeout</a>: <i>Double</i>
    <a href="#healthmonitorrefs" title="HealthMonitorRefs">HealthMonitorRefs</a>: <i>
      - String</i>
    <a href="#hostcheckenabled" title="HostCheckEnabled">HostCheckEnabled</a>: <i>Boolean</i>
    <a href="#ignoreserverport" title="IgnoreServerPort">IgnoreServerPort</a>: <i>Boolean</i>
    <a href="#ignoreservers" title="IgnoreServers">IgnoreServers</a>: <i>Boolean</i>
    <a href="#inlinehealthmonitor" title="InlineHealthMonitor">InlineHealthMonitor</a>: <i>Boolean</i>
    <a href="#ipaddrgroupref" title="IpaddrgroupRef">IpaddrgroupRef</a>: <i>String</i>
    <a href="#lbalgorithm" title="LbAlgorithm">LbAlgorithm</a>: <i>String</i>
    <a href="#lbalgorithmconsistenthashhdr" title="LbAlgorithmConsistentHashHdr">LbAlgorithmConsistentHashHdr</a>: <i>String</i>
    <a href="#lbalgorithmcorenonaffinity" title="LbAlgorithmCoreNonaffinity">LbAlgorithmCoreNonaffinity</a>: <i>Double</i>
    <a href="#lbalgorithmhash" title="LbAlgorithmHash">LbAlgorithmHash</a>: <i>String</i>
    <a href="#lookupserverbyname" title="LookupServerByName">LookupServerByName</a>: <i>Boolean</i>
    <a href="#maxconcurrentconnectionsperserver" title="MaxConcurrentConnectionsPerServer">MaxConcurrentConnectionsPerServer</a>: <i>Double</i>
    <a href="#minhealthmonitorsup" title="MinHealthMonitorsUp">MinHealthMonitorsUp</a>: <i>Double</i>
    <a href="#minserversup" title="MinServersUp">MinServersUp</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nsxsecuritygroup" title="NsxSecuritygroup">NsxSecuritygroup</a>: <i>
      - String</i>
    <a href="#pkiprofileref" title="PkiProfileRef">PkiProfileRef</a>: <i>String</i>
    <a href="#requestqueuedepth" title="RequestQueueDepth">RequestQueueDepth</a>: <i>Double</i>
    <a href="#requestqueueenabled" title="RequestQueueEnabled">RequestQueueEnabled</a>: <i>Boolean</i>
    <a href="#resolvepoolbydns" title="ResolvePoolByDns">ResolvePoolByDns</a>: <i>Boolean</i>
    <a href="#rewritehostheadertoservername" title="RewriteHostHeaderToServerName">RewriteHostHeaderToServerName</a>: <i>Boolean</i>
    <a href="#rewritehostheadertosni" title="RewriteHostHeaderToSni">RewriteHostHeaderToSni</a>: <i>Boolean</i>
    <a href="#routingpool" title="RoutingPool">RoutingPool</a>: <i>Boolean</i>
    <a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
    <a href="#servertimeout" title="ServerTimeout">ServerTimeout</a>: <i>Double</i>
    <a href="#servicemetadata" title="ServiceMetadata">ServiceMetadata</a>: <i>String</i>
    <a href="#snienabled" title="SniEnabled">SniEnabled</a>: <i>Boolean</i>
    <a href="#sslkeyandcertificateref" title="SslKeyAndCertificateRef">SslKeyAndCertificateRef</a>: <i>String</i>
    <a href="#sslprofileref" title="SslProfileRef">SslProfileRef</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#tier1lr" title="Tier1Lr">Tier1Lr</a>: <i>String</i>
    <a href="#useserviceport" title="UseServicePort">UseServicePort</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vrfref" title="VrfRef">VrfRef</a>: <i>String</i>
    <a href="#analyticspolicy" title="AnalyticsPolicy">AnalyticsPolicy</a>: <i>
      - <a href="analyticspolicydefinition.md">AnalyticsPolicyDefinition</a></i>
    <a href="#connpoolproperties" title="ConnPoolProperties">ConnPoolProperties</a>: <i>
      - <a href="connpoolpropertiesdefinition.md">ConnPoolPropertiesDefinition</a></i>
    <a href="#failaction" title="FailAction">FailAction</a>: <i>
      - <a href="failactiondefinition.md">FailActionDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#maxconnrateperserver" title="MaxConnRatePerServer">MaxConnRatePerServer</a>: <i>
      - <a href="maxconnrateperserverdefinition.md">MaxConnRatePerServerDefinition</a></i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - <a href="networksdefinition.md">NetworksDefinition</a></i>
    <a href="#placementnetworks" title="PlacementNetworks">PlacementNetworks</a>: <i>
      - <a href="placementnetworksdefinition.md">PlacementNetworksDefinition</a></i>
    <a href="#serverreselect" title="ServerReselect">ServerReselect</a>: <i>
      - <a href="serverreselectdefinition.md">ServerReselectDefinition</a></i>
    <a href="#servers" title="Servers">Servers</a>: <i>
      - <a href="serversdefinition.md">ServersDefinition</a></i>
</pre>

## Properties

#### AnalyticsProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApicEpgName

argument_description.
* `application_persistence_profile_ref` - (Optional ) argument_description.
* `autoscale_launch_config_ref` - (Optional ) argument_description.
* `autoscale_networks` - (Optional ) argument_description.
* `autoscale_policy_ref` - (Optional ) argument_description.
* `capacity_estimation` - (Optional ) argument_description.
* `capacity_estimation_ttfb_thresh` - (Optional ) argument_description.
* `cloud_config_cksum` - (Optional ) argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationPersistenceProfileRef

argument_description.
* `autoscale_launch_config_ref` - (Optional ) argument_description.
* `autoscale_networks` - (Optional ) argument_description.
* `autoscale_policy_ref` - (Optional ) argument_description.
* `capacity_estimation` - (Optional ) argument_description.
* `capacity_estimation_ttfb_thresh` - (Optional ) argument_description.
* `cloud_config_cksum` - (Optional ) argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleLaunchConfigRef

argument_description.
* `autoscale_networks` - (Optional ) argument_description.
* `autoscale_policy_ref` - (Optional ) argument_description.
* `capacity_estimation` - (Optional ) argument_description.
* `capacity_estimation_ttfb_thresh` - (Optional ) argument_description.
* `cloud_config_cksum` - (Optional ) argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscaleNetworks

argument_description.
* `autoscale_policy_ref` - (Optional ) argument_description.
* `capacity_estimation` - (Optional ) argument_description.
* `capacity_estimation_ttfb_thresh` - (Optional ) argument_description.
* `cloud_config_cksum` - (Optional ) argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoscalePolicyRef

argument_description.
* `capacity_estimation` - (Optional ) argument_description.
* `capacity_estimation_ttfb_thresh` - (Optional ) argument_description.
* `cloud_config_cksum` - (Optional ) argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityEstimation

argument_description.
* `capacity_estimation_ttfb_thresh` - (Optional ) argument_description.
* `cloud_config_cksum` - (Optional ) argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CapacityEstimationTtfbThresh

argument_description.
* `cloud_config_cksum` - (Optional ) argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudConfigCksum

argument_description.
* `cloud_ref` - (Optional ) argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudRef

argument_description.
* `connection_ramp_duration` - (Optional ) argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionRampDuration

argument_description.
* `created_by` - (Optional ) argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBy

argument_description.
* `default_server_port` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultServerPort

argument_description.
* `description` - (Optional ) argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteServerOnDnsRefresh

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

argument_description.
* `domain_name` - (Optional ) argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

argument_description.
* `east_west` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EastWest

argument_description.
* `enabled` - (Optional ) argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttp2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

argument_description.
* `external_autoscale_groups` - (Optional ) argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalAutoscaleGroups

argument_description.
* `fail_action` - (Optional ) argument_description.
* `fewest_tasks_feedback_delay` - (Optional ) argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FewestTasksFeedbackDelay

argument_description.
* `graceful_disable_timeout` - (Optional ) argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulDisableTimeout

argument_description.
* `health_monitor_refs` - (Optional ) argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthMonitorRefs

argument_description.
* `host_check_enabled` - (Optional ) argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostCheckEnabled

argument_description.
* `inline_health_monitor` - (Optional ) argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreServerPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreServers

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InlineHealthMonitor

argument_description.
* `ipaddrgroup_ref` - (Optional ) argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpaddrgroupRef

argument_description.
* `lb_algorithm` - (Optional ) argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbAlgorithm

argument_description.
* `lb_algorithm_consistent_hash_hdr` - (Optional ) argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbAlgorithmConsistentHashHdr

argument_description.
* `lb_algorithm_core_nonaffinity` - (Optional ) argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbAlgorithmCoreNonaffinity

argument_description.
* `lb_algorithm_hash` - (Optional ) argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbAlgorithmHash

argument_description.
* `lookup_server_by_name` - (Optional ) argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LookupServerByName

argument_description.
* `max_concurrent_connections_per_server` - (Optional ) argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentConnectionsPerServer

argument_description.
* `max_conn_rate_per_server` - (Optional ) argument_description.
* `name` - (Required) argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinHealthMonitorsUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinServersUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

argument_description.
* `networks` - (Optional ) argument_description.
* `nsx_securitygroup` - (Optional ) argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxSecuritygroup

argument_description.
* `pki_profile_ref` - (Optional ) argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PkiProfileRef

argument_description.
* `placement_networks` - (Optional ) argument_description.
* `request_queue_depth` - (Optional ) argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestQueueDepth

argument_description.
* `request_queue_enabled` - (Optional ) argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestQueueEnabled

argument_description.
* `rewrite_host_header_to_server_name` - (Optional ) argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolvePoolByDns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteHostHeaderToServerName

argument_description.
* `rewrite_host_header_to_sni` - (Optional ) argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteHostHeaderToSni

argument_description.
* `server_count` - (Optional ) argument_description.
* `server_name` - (Optional ) argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoutingPool

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

argument_description.
* `server_reselect` - (Optional ) argument_description.
* `servers` - (Optional ) argument_description.
* `sni_enabled` - (Optional ) argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceMetadata

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniEnabled

argument_description.
* `ssl_key_and_certificate_ref` - (Optional ) argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslKeyAndCertificateRef

argument_description.
* `ssl_profile_ref` - (Optional ) argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslProfileRef

argument_description.
* `tenant_ref` - (Optional ) argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

argument_description.
* `use_service_port` - (Optional ) argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tier1Lr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseServicePort

argument_description.
* `vrf_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrfRef

argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnalyticsPolicy

_Required_: No

_Type_: List of <a href="analyticspolicydefinition.md">AnalyticsPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnPoolProperties

_Required_: No

_Type_: List of <a href="connpoolpropertiesdefinition.md">ConnPoolPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailAction

_Required_: No

_Type_: List of <a href="failactiondefinition.md">FailActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConnRatePerServer

_Required_: No

_Type_: List of <a href="maxconnrateperserverdefinition.md">MaxConnRatePerServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

_Required_: No

_Type_: List of <a href="networksdefinition.md">NetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementNetworks

_Required_: No

_Type_: List of <a href="placementnetworksdefinition.md">PlacementNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerReselect

_Required_: No

_Type_: List of <a href="serverreselectdefinition.md">ServerReselectDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

_Required_: No

_Type_: List of <a href="serversdefinition.md">ServersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

