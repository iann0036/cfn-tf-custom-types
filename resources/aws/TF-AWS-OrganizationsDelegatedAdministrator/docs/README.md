# TF::AWS::OrganizationsDelegatedAdministrator

Provides a resource to manage an [AWS Organizations Delegated Administrator](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::OrganizationsDelegatedAdministrator",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::OrganizationsDelegatedAdministrator
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#serviceprincipal" title="ServicePrincipal">ServicePrincipal</a>: <i>String</i>
</pre>

## Properties

#### AccountId

The account ID number of the member account in the organization to register as a delegated administrator.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePrincipal

The service principal of the AWS service for which you want to make the member account a delegated administrator.

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

#### Arn

Returns the <code>Arn</code> value.

#### DelegationEnabledDate

Returns the <code>DelegationEnabledDate</code> value.

#### Email

Returns the <code>Email</code> value.

#### Id

Returns the <code>Id</code> value.

#### JoinedMethod

Returns the <code>JoinedMethod</code> value.

#### JoinedTimestamp

Returns the <code>JoinedTimestamp</code> value.

#### Name

Returns the <code>Name</code> value.

#### Status

Returns the <code>Status</code> value.

