# Terraform::AzureRM::CostManagementExportResourceGroup

Manages an Azure Cost Management Export for a Resource Group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::CostManagementExportResourceGroup",
    "Properties" : {
        "<a href="#active" title="Active">Active</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#recurrenceperiodend" title="RecurrencePeriodEnd">RecurrencePeriodEnd</a>" : <i>String</i>,
        "<a href="#recurrenceperiodstart" title="RecurrencePeriodStart">RecurrencePeriodStart</a>" : <i>String</i>,
        "<a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#deliveryinfo" title="DeliveryInfo">DeliveryInfo</a>" : <i>[ <a href="deliveryinfo.md">DeliveryInfo</a>, ... ]</i>,
        "<a href="#query" title="Query">Query</a>" : <i>[ <a href="query.md">Query</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::CostManagementExportResourceGroup
Properties:
    <a href="#active" title="Active">Active</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#recurrenceperiodend" title="RecurrencePeriodEnd">RecurrencePeriodEnd</a>: <i>String</i>
    <a href="#recurrenceperiodstart" title="RecurrencePeriodStart">RecurrencePeriodStart</a>: <i>String</i>
    <a href="#recurrencetype" title="RecurrenceType">RecurrenceType</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#deliveryinfo" title="DeliveryInfo">DeliveryInfo</a>: <i>
      - <a href="deliveryinfo.md">DeliveryInfo</a></i>
    <a href="#query" title="Query">Query</a>: <i>
      - <a href="query.md">Query</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Active

Is the cost management export active? Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Cost Management Export. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrencePeriodEnd

The date the export will stop capturing information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrencePeriodStart

The date the export will start capturing information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecurrenceType

How often the requested information will be exported. Valid values include `Annually`, `Daily`, `Monthly`, `Weekly`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The id of the resource group in which to export information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeliveryInfo

_Required_: No

_Type_: List of <a href="deliveryinfo.md">DeliveryInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No

_Type_: List of <a href="query.md">Query</a>

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

