# TF::AzureRM::AppServiceEnvironment

Manages an App Service Environment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureRM::AppServiceEnvironment",
    "Properties" : {
        "<a href="#alloweduseripcidrs" title="AllowedUserIpCidrs">AllowedUserIpCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#frontendscalefactor" title="FrontEndScaleFactor">FrontEndScaleFactor</a>" : <i>Double</i>,
        "<a href="#internalloadbalancingmode" title="InternalLoadBalancingMode">InternalLoadBalancingMode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pricingtier" title="PricingTier">PricingTier</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#userwhitelistedipranges" title="UserWhitelistedIpRanges">UserWhitelistedIpRanges</a>" : <i>[ String, ... ]</i>,
        "<a href="#clustersetting" title="ClusterSetting">ClusterSetting</a>" : <i>[ <a href="clustersettingdefinition.md">ClusterSettingDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureRM::AppServiceEnvironment
Properties:
    <a href="#alloweduseripcidrs" title="AllowedUserIpCidrs">AllowedUserIpCidrs</a>: <i>
      - String</i>
    <a href="#frontendscalefactor" title="FrontEndScaleFactor">FrontEndScaleFactor</a>: <i>Double</i>
    <a href="#internalloadbalancingmode" title="InternalLoadBalancingMode">InternalLoadBalancingMode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pricingtier" title="PricingTier">PricingTier</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#userwhitelistedipranges" title="UserWhitelistedIpRanges">UserWhitelistedIpRanges</a>: <i>
      - String</i>
    <a href="#clustersetting" title="ClusterSetting">ClusterSetting</a>: <i>
      - <a href="clustersettingdefinition.md">ClusterSettingDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AllowedUserIpCidrs

Allowed user added IP ranges on the ASE database. Use the addresses you want to set as the explicit egress address ranges.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontEndScaleFactor

Scale factor for front end instances. Possible values are between `5` and `15`. Defaults to `15`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalLoadBalancingMode

Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment. Possible values are `None`, `Web`, `Publishing` and combined value `"Web, Publishing"`. Defaults to `None`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the App Service Environment. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PricingTier

Pricing tier for the front end instances. Possible values are `I1`, `I2` and `I3`. Defaults to `I1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group where the App Service Environment exists. Defaults to the Resource Group of the Subnet (specified by `subnet_id`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

The ID of the Subnet which the App Service Environment should be connected to. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserWhitelistedIpRanges

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterSetting

_Required_: No

_Type_: List of <a href="clustersettingdefinition.md">ClusterSettingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### InternalIpAddress

Returns the <code>InternalIpAddress</code> value.

#### Location

Returns the <code>Location</code> value.

#### OutboundIpAddresses

Returns the <code>OutboundIpAddresses</code> value.

#### ServiceIpAddress

Returns the <code>ServiceIpAddress</code> value.

