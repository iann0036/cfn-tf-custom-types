# TF::AzureRM::NetworkWatcherFlowLog TrafficAnalyticsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#intervalinminutes" title="IntervalInMinutes">IntervalInMinutes</a>" : <i>Double</i>,
    "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>String</i>,
    "<a href="#workspaceregion" title="WorkspaceRegion">WorkspaceRegion</a>" : <i>String</i>,
    "<a href="#workspaceresourceid" title="WorkspaceResourceId">WorkspaceResourceId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#intervalinminutes" title="IntervalInMinutes">IntervalInMinutes</a>: <i>Double</i>
<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>String</i>
<a href="#workspaceregion" title="WorkspaceRegion">WorkspaceRegion</a>: <i>String</i>
<a href="#workspaceresourceid" title="WorkspaceResourceId">WorkspaceResourceId</a>: <i>String</i>
</pre>

## Properties

#### Enabled

Boolean flag to enable/disable traffic analytics.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalInMinutes

How frequently service should do flow analytics in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceId

The resource guid of the attached workspace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceRegion

The location of the attached workspace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceResourceId

The resource ID of the attached workspace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

