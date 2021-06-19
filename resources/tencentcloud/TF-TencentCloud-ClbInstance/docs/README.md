# TF::TencentCloud::ClbInstance

Provides a resource to create a CLB instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ClbInstance",
    "Properties" : {
        "<a href="#addressipversion" title="AddressIpVersion">AddressIpVersion</a>" : <i>String</i>,
        "<a href="#clbname" title="ClbName">ClbName</a>" : <i>String</i>,
        "<a href="#internetbandwidthmaxout" title="InternetBandwidthMaxOut">InternetBandwidthMaxOut</a>" : <i>Double</i>,
        "<a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>" : <i>String</i>,
        "<a href="#loadbalancerpasstotarget" title="LoadBalancerPassToTarget">LoadBalancerPassToTarget</a>" : <i>Boolean</i>,
        "<a href="#masterzoneid" title="MasterZoneId">MasterZoneId</a>" : <i>String</i>,
        "<a href="#networktype" title="NetworkType">NetworkType</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>Double</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#slavezoneid" title="SlaveZoneId">SlaveZoneId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#targetregioninforegion" title="TargetRegionInfoRegion">TargetRegionInfoRegion</a>" : <i>String</i>,
        "<a href="#targetregioninfovpcid" title="TargetRegionInfoVpcId">TargetRegionInfoVpcId</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ClbInstance
Properties:
    <a href="#addressipversion" title="AddressIpVersion">AddressIpVersion</a>: <i>String</i>
    <a href="#clbname" title="ClbName">ClbName</a>: <i>String</i>
    <a href="#internetbandwidthmaxout" title="InternetBandwidthMaxOut">InternetBandwidthMaxOut</a>: <i>Double</i>
    <a href="#internetchargetype" title="InternetChargeType">InternetChargeType</a>: <i>String</i>
    <a href="#loadbalancerpasstotarget" title="LoadBalancerPassToTarget">LoadBalancerPassToTarget</a>: <i>Boolean</i>
    <a href="#masterzoneid" title="MasterZoneId">MasterZoneId</a>: <i>String</i>
    <a href="#networktype" title="NetworkType">NetworkType</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>Double</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#slavezoneid" title="SlaveZoneId">SlaveZoneId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#targetregioninforegion" title="TargetRegionInfoRegion">TargetRegionInfoRegion</a>: <i>String</i>
    <a href="#targetregioninfovpcid" title="TargetRegionInfoVpcId">TargetRegionInfoVpcId</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### AddressIpVersion

IP version, only applicable to open CLB. Valid values are `ipv4`, `ipv6` and `IPv6FullChain`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClbName

Name of the CLB. The name can only contain Chinese characters, English letters, numbers, underscore and hyphen '-'.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetBandwidthMaxOut

Max bandwidth out, only applicable to open CLB. Valid value ranges is [1, 2048]. Unit is MB.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternetChargeType

Internet charge type, only applicable to open CLB. Valid values are `TRAFFIC_POSTPAID_BY_HOUR`, `BANDWIDTH_POSTPAID_BY_HOUR` and `BANDWIDTH_PACKAGE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerPassToTarget

Whether the target allow flow come from clb. If value is true, only check security group of clb, or check both clb and backend instance security group.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterZoneId

Setting master zone id of cross available zone disaster recovery, only applicable to open CLB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkType

Type of CLB instance. Valid values: `OPEN` and `INTERNAL`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

ID of the project within the CLB instance, `0` - Default Project.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

Security groups of the CLB instance. Supports both `OPEN` and `INTERNAL` CLBs.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaveZoneId

Setting slave zone id of cross available zone disaster recovery, only applicable to open CLB. this zone will undertake traffic when the master is down.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

Subnet ID of the CLB. Effective only for CLB within the VPC. Only supports `INTERNAL` CLBs. Default is `ipv4`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

The available tags within this CLB.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRegionInfoRegion

Region information of backend services are attached the CLB instance. Only supports `OPEN` CLBs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRegionInfoVpcId

Vpc information of backend services are attached the CLB instance. Only supports `OPEN` CLBs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC ID of the CLB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

Available zone id, only applicable to open CLB.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ClbVips

Returns the <code>ClbVips</code> value.

#### Id

Returns the <code>Id</code> value.

#### VipIsp

Returns the <code>VipIsp</code> value.

