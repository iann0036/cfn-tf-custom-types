# TF::AzureRM::MonitorActionGroup ItsmReceiverDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectionid" title="ConnectionId">ConnectionId</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#ticketconfiguration" title="TicketConfiguration">TicketConfiguration</a>" : <i>String</i>,
    "<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#connectionid" title="ConnectionId">ConnectionId</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#ticketconfiguration" title="TicketConfiguration">TicketConfiguration</a>: <i>String</i>
<a href="#workspaceid" title="WorkspaceId">WorkspaceId</a>: <i>String</i>
</pre>

## Properties

#### ConnectionId

The unique connection identifier of the ITSM connection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the ITSM receiver.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region of the workspace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TicketConfiguration

A JSON blob for the configurations of the ITSM action. CreateMultipleWorkItems option will be part of this blob as well.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkspaceId

The Azure Log Analytics workspace ID where this connection is defined.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

