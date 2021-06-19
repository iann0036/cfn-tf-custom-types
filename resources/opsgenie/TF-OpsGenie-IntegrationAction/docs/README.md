# TF::OpsGenie::IntegrationAction

Manages advanced actions for Integrations within Opsgenie. This applies for the following resources:
* [`opsgenie_api_integration`](api_integration.html)
* [`opsgenie_email_integration`](email_integration.html)

The actions that are supported are:
* `create`
* `close`
* `acknowledge`
* `add_note`
* `ignore`

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::IntegrationAction",
    "Properties" : {
        "<a href="#integrationid" title="IntegrationId">IntegrationId</a>" : <i>String</i>,
        "<a href="#acknowledge" title="Acknowledge">Acknowledge</a>" : <i>[ <a href="acknowledgedefinition.md">AcknowledgeDefinition</a>, ... ]</i>,
        "<a href="#addnote" title="AddNote">AddNote</a>" : <i>[ <a href="addnotedefinition.md">AddNoteDefinition</a>, ... ]</i>,
        "<a href="#close" title="Close">Close</a>" : <i>[ <a href="closedefinition.md">CloseDefinition</a>, ... ]</i>,
        "<a href="#create" title="Create">Create</a>" : <i>[ <a href="createdefinition.md">CreateDefinition</a>, ... ]</i>,
        "<a href="#ignore" title="Ignore">Ignore</a>" : <i>[ <a href="ignoredefinition.md">IgnoreDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::IntegrationAction
Properties:
    <a href="#integrationid" title="IntegrationId">IntegrationId</a>: <i>String</i>
    <a href="#acknowledge" title="Acknowledge">Acknowledge</a>: <i>
      - <a href="acknowledgedefinition.md">AcknowledgeDefinition</a></i>
    <a href="#addnote" title="AddNote">AddNote</a>: <i>
      - <a href="addnotedefinition.md">AddNoteDefinition</a></i>
    <a href="#close" title="Close">Close</a>: <i>
      - <a href="closedefinition.md">CloseDefinition</a></i>
    <a href="#create" title="Create">Create</a>: <i>
      - <a href="createdefinition.md">CreateDefinition</a></i>
    <a href="#ignore" title="Ignore">Ignore</a>: <i>
      - <a href="ignoredefinition.md">IgnoreDefinition</a></i>
</pre>

## Properties

#### IntegrationId

ID of the parent integration resource to bind to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acknowledge

_Required_: No

_Type_: List of <a href="acknowledgedefinition.md">AcknowledgeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddNote

_Required_: No

_Type_: List of <a href="addnotedefinition.md">AddNoteDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Close

_Required_: No

_Type_: List of <a href="closedefinition.md">CloseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Create

_Required_: No

_Type_: List of <a href="createdefinition.md">CreateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ignore

_Required_: No

_Type_: List of <a href="ignoredefinition.md">IgnoreDefinition</a>

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

