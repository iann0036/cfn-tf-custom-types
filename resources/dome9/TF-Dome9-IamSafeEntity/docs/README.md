# TF::Dome9::IamSafeEntity

Protect cloud accounts that are managed by Dome9. Control access to them with targeted short-term authorizations (involving the Dome9 mobile app).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::IamSafeEntity",
    "Properties" : {
        "<a href="#awscloudaccountid" title="AwsCloudAccountId">AwsCloudAccountId</a>" : <i>String</i>,
        "<a href="#dome9usersidtoprotect" title="Dome9UsersIdToProtect">Dome9UsersIdToProtect</a>" : <i>[ String, ... ]</i>,
        "<a href="#entityname" title="EntityName">EntityName</a>" : <i>String</i>,
        "<a href="#entitytype" title="EntityType">EntityType</a>" : <i>String</i>,
        "<a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::IamSafeEntity
Properties:
    <a href="#awscloudaccountid" title="AwsCloudAccountId">AwsCloudAccountId</a>: <i>String</i>
    <a href="#dome9usersidtoprotect" title="Dome9UsersIdToProtect">Dome9UsersIdToProtect</a>: <i>
      - String</i>
    <a href="#entityname" title="EntityName">EntityName</a>: <i>String</i>
    <a href="#entitytype" title="EntityType">EntityType</a>: <i>String</i>
    <a href="#protectionmode" title="ProtectionMode">ProtectionMode</a>: <i>String</i>
</pre>

## Properties

#### AwsCloudAccountId

AWS cloud account id to protect.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dome9UsersIdToProtect

When ProtectWithElevation mode selected, dome9 users ids must be provided.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityName

AWS IAM user or role name to protect.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntityType

Entity type to protect; can be  "User", "Role".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectionMode

Protection mode; can be  "Protect", "ProtectWithElevation".

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

#### AttachedDome9Users

Returns the <code>AttachedDome9Users</code> value.

#### ExistsInAws

Returns the <code>ExistsInAws</code> value.

#### Id

Returns the <code>Id</code> value.

#### State

Returns the <code>State</code> value.

