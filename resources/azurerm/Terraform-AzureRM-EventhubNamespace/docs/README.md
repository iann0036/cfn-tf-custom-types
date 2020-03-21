# Terraform::AzureRM::EventhubNamespace

Manages an EventHub Namespace.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::EventhubNamespace",
    "Properties" : {
        "<a href="#autoinflateenabled" title="AutoInflateEnabled">AutoInflateEnabled</a>" : <i>Boolean</i>,
        "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#maximumthroughputunits" title="MaximumThroughputUnits">MaximumThroughputUnits</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkrulesets" title="NetworkRulesets">NetworkRulesets</a>" : <i>[ <a href="networkrulesets.md">NetworkRulesets</a>, ... ]</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::EventhubNamespace
Properties:
    <a href="#autoinflateenabled" title="AutoInflateEnabled">AutoInflateEnabled</a>: <i>Boolean</i>
    <a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#maximumthroughputunits" title="MaximumThroughputUnits">MaximumThroughputUnits</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkrulesets" title="NetworkRulesets">NetworkRulesets</a>: <i>
      - <a href="networkrulesets.md">NetworkRulesets</a></i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#sku" title="Sku">Sku</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AutoInflateEnabled

Is Auto Inflate enabled for the EventHub Namespace?.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

Specifies the Capacity / Throughput Units for a `Standard` SKU namespace. Valid values range from `1` - `20`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumThroughputUnits

Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from `1` - `20`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkRulesets

A `network_rulesets` block as defined below.

_Required_: No

_Type_: List of <a href="networkrulesets.md">NetworkRulesets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

Defines which tier to use. Valid options are `Basic` and `Standard`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultPrimaryConnectionString

Returns the <code>DefaultPrimaryConnectionString</code> value.

#### DefaultPrimaryKey

Returns the <code>DefaultPrimaryKey</code> value.

#### DefaultSecondaryConnectionString

Returns the <code>DefaultSecondaryConnectionString</code> value.

#### DefaultSecondaryKey

Returns the <code>DefaultSecondaryKey</code> value.

