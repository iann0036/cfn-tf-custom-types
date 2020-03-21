# Terraform::AzureRM::MonitorActivityLogAlert Criteria

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#caller" title="Caller">Caller</a>" : <i>String</i>,
    "<a href="#category" title="Category">Category</a>" : <i>String</i>,
    "<a href="#level" title="Level">Level</a>" : <i>String</i>,
    "<a href="#operationname" title="OperationName">OperationName</a>" : <i>String</i>,
    "<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>" : <i>String</i>,
    "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
    "<a href="#resourceprovider" title="ResourceProvider">ResourceProvider</a>" : <i>String</i>,
    "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#substatus" title="SubStatus">SubStatus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#caller" title="Caller">Caller</a>: <i>String</i>
<a href="#category" title="Category">Category</a>: <i>String</i>
<a href="#level" title="Level">Level</a>: <i>String</i>
<a href="#operationname" title="OperationName">OperationName</a>: <i>String</i>
<a href="#resourcegroup" title="ResourceGroup">ResourceGroup</a>: <i>String</i>
<a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
<a href="#resourceprovider" title="ResourceProvider">ResourceProvider</a>: <i>String</i>
<a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#substatus" title="SubStatus">SubStatus</a>: <i>String</i>
</pre>

## Properties

#### Caller

The email address or Azure Active Directory identifier of the user who performed the operation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Category

The category of the operation. Possible values are `Administrative`, `Autoscale`, `Policy`, `Recommendation`, `ResourceHealth`, `Security` and `ServiceHealth`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

The severity level of the event. Possible values are `Verbose`, `Informational`, `Warning`, `Error`, and `Critical`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationName

The Resource Manager Role-Based Access Control operation name. Supported operation should be of the form: `<resourceProvider>/<resourceType>/<operation>`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroup

The name of resource group monitored by the activity log alert.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceId

The specific resource monitored by the activity log alert. It should be within one of the `scopes`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceProvider

The name of the resource provider monitored by the activity log alert.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

The resource type monitored by the activity log alert.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the event. For example, `Started`, `Failed`, or `Succeeded`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubStatus

The sub status of the event.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

