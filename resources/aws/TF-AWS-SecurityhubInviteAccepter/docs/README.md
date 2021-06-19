# TF::AWS::SecurityhubInviteAccepter

-> **Note:** AWS accounts can only be associated with a single Security Hub master account. Destroying this resource will disassociate the member account from the master account.

Accepts a Security Hub invitation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SecurityhubInviteAccepter",
    "Properties" : {
        "<a href="#masterid" title="MasterId">MasterId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SecurityhubInviteAccepter
Properties:
    <a href="#masterid" title="MasterId">MasterId</a>: <i>String</i>
</pre>

## Properties

#### MasterId

The account ID of the master Security Hub account whose invitation you're accepting.

_Required_: Yes

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

#### InvitationId

Returns the <code>InvitationId</code> value.

