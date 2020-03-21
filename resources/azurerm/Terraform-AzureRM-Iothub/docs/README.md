# Terraform::AzureRM::Iothub

CloudFormation equivalent of azurerm_iothub

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::Iothub",
    "Properties" : {
        "<a href="#eventhubpartitioncount" title="EventHubPartitionCount">EventHubPartitionCount</a>" : <i>Double</i>,
        "<a href="#eventhubretentionindays" title="EventHubRetentionInDays">EventHubRetentionInDays</a>" : <i>Double</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>[ <a href="endpoint.md">Endpoint</a>, ... ]</i>,
        "<a href="#fallbackroute" title="FallbackRoute">FallbackRoute</a>" : <i>[ <a href="fallbackroute.md">FallbackRoute</a>, ... ]</i>,
        "<a href="#fileupload" title="FileUpload">FileUpload</a>" : <i>[ <a href="fileupload.md">FileUpload</a>, ... ]</i>,
        "<a href="#ipfilterrule" title="IpFilterRule">IpFilterRule</a>" : <i>[ <a href="ipfilterrule.md">IpFilterRule</a>, ... ]</i>,
        "<a href="#route" title="Route">Route</a>" : <i>[ <a href="route.md">Route</a>, ... ]</i>,
        "<a href="#sku" title="Sku">Sku</a>" : <i>[ <a href="sku.md">Sku</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::Iothub
Properties:
    <a href="#eventhubpartitioncount" title="EventHubPartitionCount">EventHubPartitionCount</a>: <i>Double</i>
    <a href="#eventhubretentionindays" title="EventHubRetentionInDays">EventHubRetentionInDays</a>: <i>Double</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#endpoint" title="Endpoint">Endpoint</a>: <i>
      - <a href="endpoint.md">Endpoint</a></i>
    <a href="#fallbackroute" title="FallbackRoute">FallbackRoute</a>: <i>
      - <a href="fallbackroute.md">FallbackRoute</a></i>
    <a href="#fileupload" title="FileUpload">FileUpload</a>: <i>
      - <a href="fileupload.md">FileUpload</a></i>
    <a href="#ipfilterrule" title="IpFilterRule">IpFilterRule</a>: <i>
      - <a href="ipfilterrule.md">IpFilterRule</a></i>
    <a href="#route" title="Route">Route</a>: <i>
      - <a href="route.md">Route</a></i>
    <a href="#sku" title="Sku">Sku</a>: <i>
      - <a href="sku.md">Sku</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### EventHubPartitionCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventHubRetentionInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: No

_Type_: List of <a href="endpoint.md">Endpoint</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FallbackRoute

_Required_: No

_Type_: List of <a href="fallbackroute.md">FallbackRoute</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUpload

_Required_: No

_Type_: List of <a href="fileupload.md">FileUpload</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpFilterRule

_Required_: No

_Type_: List of <a href="ipfilterrule.md">IpFilterRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Route

_Required_: No

_Type_: List of <a href="route.md">Route</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sku

_Required_: No

_Type_: List of <a href="sku.md">Sku</a>

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

#### EventHubEventsEndpoint

Returns the <code>EventHubEventsEndpoint</code> value.

#### EventHubEventsPath

Returns the <code>EventHubEventsPath</code> value.

#### EventHubOperationsEndpoint

Returns the <code>EventHubOperationsEndpoint</code> value.

#### EventHubOperationsPath

Returns the <code>EventHubOperationsPath</code> value.

#### Hostname

Returns the <code>Hostname</code> value.

#### SharedAccessPolicy

Returns the <code>SharedAccessPolicy</code> value.

#### Type

Returns the <code>Type</code> value.

