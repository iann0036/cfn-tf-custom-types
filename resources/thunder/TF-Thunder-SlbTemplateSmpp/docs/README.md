# TF::Thunder::SlbTemplateSmpp

`thunder_slb_template_smpp` Provides details about thunder slb template smpp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateSmpp",
    "Properties" : {
        "<a href="#clientenquirelink" title="ClientEnquireLink">ClientEnquireLink</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#serverenquirelink" title="ServerEnquireLink">ServerEnquireLink</a>" : <i>Double</i>,
        "<a href="#serverenquirelinkval" title="ServerEnquireLinkVal">ServerEnquireLinkVal</a>" : <i>Double</i>,
        "<a href="#serverselectionperrequest" title="ServerSelectionPerRequest">ServerSelectionPerRequest</a>" : <i>Double</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateSmpp
Properties:
    <a href="#clientenquirelink" title="ClientEnquireLink">ClientEnquireLink</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#serverenquirelink" title="ServerEnquireLink">ServerEnquireLink</a>: <i>Double</i>
    <a href="#serverenquirelinkval" title="ServerEnquireLinkVal">ServerEnquireLinkVal</a>: <i>Double</i>
    <a href="#serverselectionperrequest" title="ServerSelectionPerRequest">ServerSelectionPerRequest</a>: <i>Double</i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### ClientEnquireLink

Respond client ENQUIRE_LINK packet directly instead of forwarding to server.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SMPP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Configure the password used to bind.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerEnquireLink

Send server ENQUIRE_LINK packet for every persist connection when enable conn-reuse.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerEnquireLinkVal

Set interval of keep-alive packet for each persistent connection (second, default is 30).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSelectionPerRequest

Force server selection on every SMPP request when enable conn-reuse.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

Configure the user to bind (The name used to bind).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

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

#### Id

Returns the <code>Id</code> value.

