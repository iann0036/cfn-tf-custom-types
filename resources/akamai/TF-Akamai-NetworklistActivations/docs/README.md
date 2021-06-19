# TF::Akamai::NetworklistActivations

Use the `akamai_networklist_activations` resource to activate a network list in either the STAGING or PRODUCTION
environment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::NetworklistActivations",
    "Properties" : {
        "<a href="#activate" title="Activate">Activate</a>" : <i>Boolean</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#networklistid" title="NetworkListId">NetworkListId</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::NetworklistActivations
Properties:
    <a href="#activate" title="Activate">Activate</a>: <i>Boolean</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#networklistid" title="NetworkListId">NetworkListId</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#notificationemails" title="NotificationEmails">NotificationEmails</a>: <i>
      - String</i>
</pre>

## Properties

#### Activate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

The network to be used, either `STAGING` or `PRODUCTION`. If not supplied, defaults to
`STAGING`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkListId

The ID of the network list to be activated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

A comment describing the activation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationEmails

A bracketed, comma-separated list of email addresses that will be notified when the
operation is complete.

_Required_: Yes

_Type_: List of String

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

#### Status

Returns the <code>Status</code> value.

