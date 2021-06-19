# TF::ECL::SssApprovalRequestV1

Manages a V2 Approval Request resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::SssApprovalRequestV1",
    "Properties" : {
        "<a href="#requestid" title="RequestId">RequestId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::SssApprovalRequestV1
Properties:
    <a href="#requestid" title="RequestId">RequestId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### RequestId

tenant_connection_request unique ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Modify status of the approval request.(approved/denied/cancelled) Request’s status can only change from ‘registerd’.

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

#### Actions

Returns the <code>Actions</code> value.

#### ApprovalDeadline

Returns the <code>ApprovalDeadline</code> value.

#### ApprovalExpire

Returns the <code>ApprovalExpire</code> value.

#### Approver

Returns the <code>Approver</code> value.

#### ApproverId

Returns the <code>ApproverId</code> value.

#### ApproverType

Returns the <code>ApproverType</code> value.

#### Descriptions

Returns the <code>Descriptions</code> value.

#### ExternalRequestId

Returns the <code>ExternalRequestId</code> value.

#### Id

Returns the <code>Id</code> value.

#### RegisteredTime

Returns the <code>RegisteredTime</code> value.

#### RequestUser

Returns the <code>RequestUser</code> value.

#### RequestUserId

Returns the <code>RequestUserId</code> value.

#### Service

Returns the <code>Service</code> value.

#### UpdatedTime

Returns the <code>UpdatedTime</code> value.

