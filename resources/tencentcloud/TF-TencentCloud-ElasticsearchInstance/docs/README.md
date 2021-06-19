# TF::TencentCloud::ElasticsearchInstance

Provides an elasticsearch instance resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ElasticsearchInstance",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#basicsecuritytype" title="BasicSecurityType">BasicSecurityType</a>" : <i>Double</i>,
        "<a href="#chargeperiod" title="ChargePeriod">ChargePeriod</a>" : <i>Double</i>,
        "<a href="#chargetype" title="ChargeType">ChargeType</a>" : <i>String</i>,
        "<a href="#deploymode" title="DeployMode">DeployMode</a>" : <i>Double</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#renewflag" title="RenewFlag">RenewFlag</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#multizoneinfos" title="MultiZoneInfos">MultiZoneInfos</a>" : <i>[ <a href="multizoneinfosdefinition.md">MultiZoneInfosDefinition</a>, ... ]</i>,
        "<a href="#nodeinfolist" title="NodeInfoList">NodeInfoList</a>" : <i>[ <a href="nodeinfolistdefinition.md">NodeInfoListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ElasticsearchInstance
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#basicsecuritytype" title="BasicSecurityType">BasicSecurityType</a>: <i>Double</i>
    <a href="#chargeperiod" title="ChargePeriod">ChargePeriod</a>: <i>Double</i>
    <a href="#chargetype" title="ChargeType">ChargeType</a>: <i>String</i>
    <a href="#deploymode" title="DeployMode">DeployMode</a>: <i>Double</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#renewflag" title="RenewFlag">RenewFlag</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#multizoneinfos" title="MultiZoneInfos">MultiZoneInfos</a>: <i>
      - <a href="multizoneinfosdefinition.md">MultiZoneInfosDefinition</a></i>
    <a href="#nodeinfolist" title="NodeInfoList">NodeInfoList</a>: <i>
      - <a href="nodeinfolistdefinition.md">NodeInfoListDefinition</a></i>
</pre>

## Properties

#### AvailabilityZone

Availability zone.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BasicSecurityType

Whether to enable X-Pack security authentication in Basic Edition 6.8 and above. Valid values are `1` and `2`. `1` is disabled, `2` is enabled, and default value is `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargePeriod

The tenancy of the prepaid instance, and uint is month. NOTE: it only works when charge_type is set to `PREPAID`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChargeType

The charge type of instance. Valid values are `PREPAID` and `POSTPAID_BY_HOUR`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeployMode

Cluster deployment mode. Valid values are `0` and `1`. `0` is single-AZ deployment, and `1` is multi-AZ deployment. Default value is `0`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

Name of the instance, which can contain 1 to 50 English letters, Chinese characters, digits, dashes(-), or underscores(_).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

License type. Valid values are `oss`, `basic` and `platinum`. The default value is `platinum`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password to an instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenewFlag

When enabled, the instance will be renew automatically when it reach the end of the prepaid tenancy. Valid values are `RENEW_FLAG_AUTO` and `RENEW_FLAG_MANUAL`. NOTE: it only works when charge_type is set to `PREPAID`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of a VPC subnetwork.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the instance. For tag limits, please refer to [Use Limits](https://intl.cloud.tencent.com/document/product/651/13354).

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Version of the instance. Valid values are `5.6.4`, `6.4.3`, `6.8.2` and `7.5.1`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The ID of a VPC network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiZoneInfos

_Required_: No

_Type_: List of <a href="multizoneinfosdefinition.md">MultiZoneInfosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeInfoList

_Required_: No

_Type_: List of <a href="nodeinfolistdefinition.md">NodeInfoListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### ElasticsearchDomain

Returns the <code>ElasticsearchDomain</code> value.

#### ElasticsearchPort

Returns the <code>ElasticsearchPort</code> value.

#### ElasticsearchVip

Returns the <code>ElasticsearchVip</code> value.

#### Id

Returns the <code>Id</code> value.

#### KibanaUrl

Returns the <code>KibanaUrl</code> value.

