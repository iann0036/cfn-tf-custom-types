# TF::AVI::Gslbservice

The GslbService resource allows the creation and management of Avi GslbService

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Gslbservice",
    "Properties" : {
        "<a href="#applicationpersistenceprofileref" title="ApplicationPersistenceProfileRef">ApplicationPersistenceProfileRef</a>" : <i>String</i>,
        "<a href="#controllerhealthstatusenabled" title="ControllerHealthStatusEnabled">ControllerHealthStatusEnabled</a>" : <i>Boolean</i>,
        "<a href="#createdby" title="CreatedBy">CreatedBy</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domainnames" title="DomainNames">DomainNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#healthmonitorrefs" title="HealthMonitorRefs">HealthMonitorRefs</a>" : <i>[ String, ... ]</i>,
        "<a href="#healthmonitorscope" title="HealthMonitorScope">HealthMonitorScope</a>" : <i>String</i>,
        "<a href="#hmoff" title="HmOff">HmOff</a>" : <i>Boolean</i>,
        "<a href="#isfederated" title="IsFederated">IsFederated</a>" : <i>Boolean</i>,
        "<a href="#minmembers" title="MinMembers">MinMembers</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numdnsip" title="NumDnsIp">NumDnsIp</a>" : <i>Double</i>,
        "<a href="#poolalgorithm" title="PoolAlgorithm">PoolAlgorithm</a>" : <i>String</i>,
        "<a href="#resolvecname" title="ResolveCname">ResolveCname</a>" : <i>Boolean</i>,
        "<a href="#sitepersistenceenabled" title="SitePersistenceEnabled">SitePersistenceEnabled</a>" : <i>Boolean</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#useednsclientsubnet" title="UseEdnsClientSubnet">UseEdnsClientSubnet</a>" : <i>Boolean</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#wildcardmatch" title="WildcardMatch">WildcardMatch</a>" : <i>Boolean</i>,
        "<a href="#downresponse" title="DownResponse">DownResponse</a>" : <i>[ <a href="downresponsedefinition.md">DownResponseDefinition</a>, ... ]</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ <a href="groupsdefinition.md">GroupsDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Gslbservice
Properties:
    <a href="#applicationpersistenceprofileref" title="ApplicationPersistenceProfileRef">ApplicationPersistenceProfileRef</a>: <i>String</i>
    <a href="#controllerhealthstatusenabled" title="ControllerHealthStatusEnabled">ControllerHealthStatusEnabled</a>: <i>Boolean</i>
    <a href="#createdby" title="CreatedBy">CreatedBy</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domainnames" title="DomainNames">DomainNames</a>: <i>
      - String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#healthmonitorrefs" title="HealthMonitorRefs">HealthMonitorRefs</a>: <i>
      - String</i>
    <a href="#healthmonitorscope" title="HealthMonitorScope">HealthMonitorScope</a>: <i>String</i>
    <a href="#hmoff" title="HmOff">HmOff</a>: <i>Boolean</i>
    <a href="#isfederated" title="IsFederated">IsFederated</a>: <i>Boolean</i>
    <a href="#minmembers" title="MinMembers">MinMembers</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numdnsip" title="NumDnsIp">NumDnsIp</a>: <i>Double</i>
    <a href="#poolalgorithm" title="PoolAlgorithm">PoolAlgorithm</a>: <i>String</i>
    <a href="#resolvecname" title="ResolveCname">ResolveCname</a>: <i>Boolean</i>
    <a href="#sitepersistenceenabled" title="SitePersistenceEnabled">SitePersistenceEnabled</a>: <i>Boolean</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#useednsclientsubnet" title="UseEdnsClientSubnet">UseEdnsClientSubnet</a>: <i>Boolean</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#wildcardmatch" title="WildcardMatch">WildcardMatch</a>: <i>Boolean</i>
    <a href="#downresponse" title="DownResponse">DownResponse</a>: <i>
      - <a href="downresponsedefinition.md">DownResponseDefinition</a></i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - <a href="groupsdefinition.md">GroupsDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
</pre>

## Properties

#### ApplicationPersistenceProfileRef

The federated application persistence associated with gslbservice site persistence functionality. It is a reference to an object of type applicationpersistenceprofile. Field introduced in 17.2.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControllerHealthStatusEnabled

Gs member's overall health status is derived based on a combination of controller and datapath health-status inputs. Note that the datapath status is determined by the association of health monitor profiles. Only the controller provided status is determined through this configuration.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatedBy

Creator name. Field introduced in 17.1.2.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNames

Fully qualified domain name of the gslb service. Minimum of 1 items required.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable or disable the gslb service. If the gslb service is enabled, then the vips are sent in the dns responses based on reachability and configured algorithm. If the gslb service is disabled, then the vips are no longer available in the dns response.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthMonitorRefs

Verify vs health by applying one or more health monitors. Active monitors generate synthetic traffic from dns service engine and to mark a vs up or down based on the response. It is a reference to an object of type healthmonitor. Maximum of 6 items allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthMonitorScope

Health monitor probe can be executed for all the members or it can be executed only for third-party members. This operational mode is useful to reduce the number of health monitor probes in case of a hybrid scenario. In such a case, avi members can have controller derived status while non-avi members can be probed by via health monitor probes in dataplane. Enum options - GSLB_SERVICE_HEALTH_MONITOR_ALL_MEMBERS, GSLB_SERVICE_HEALTH_MONITOR_ONLY_NON_AVI_MEMBERS.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HmOff

This field is an internal field and is used in se. Field introduced in 18.2.2.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFederated

This field indicates that this object is replicated across gslb federation. Field introduced in 17.1.3.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinMembers

The minimum number of members to distribute traffic to. Allowed values are 1-65535. Special values are 0 - 'disable'. Field introduced in 17.2.4.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name for the gslb service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumDnsIp

Number of ip addresses of this gslb service to be returned by the dns service. Enter 0 to return all ip addresses. Allowed values are 1-20. Special values are 0- 'return all ip addresses'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolAlgorithm

The load balancing algorithm will pick a gslb pool within the gslb service list of available pools. Enum options - GSLB_SERVICE_ALGORITHM_PRIORITY, GSLB_SERVICE_ALGORITHM_GEO. Field introduced in 17.2.3.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveCname

This field indicates that for a cname query, respond with resolved cnames in the additional section with a records. Field introduced in 18.2.5.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SitePersistenceEnabled

Enable site-persistence for the gslbservice. Field introduced in 17.2.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

Ttl value (in seconds) for records served for this gslb service by the dns service. Allowed values are 0-86400. Unit is sec.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseEdnsClientSubnet

Use the client ip subnet from the edns option as source ipaddress for client geo-location and consistent hash algorithm. Default is true. Field introduced in 17.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildcardMatch

Enable wild-card match of fqdn  if an exact match is not found in the dns table, the longest match is chosen by wild-carding the fqdn in the dns request. Default is false. Field introduced in 17.1.1.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownResponse

_Required_: No

_Type_: List of <a href="downresponsedefinition.md">DownResponseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of <a href="groupsdefinition.md">GroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

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

