# TF::OpsGenie::CustomRole

Manages custom user roles within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::CustomRole",
    "Properties" : {
        "<a href="#disallowedrights" title="DisallowedRights">DisallowedRights</a>" : <i>[ String, ... ]</i>,
        "<a href="#extendedrole" title="ExtendedRole">ExtendedRole</a>" : <i>String</i>,
        "<a href="#grantedrights" title="GrantedRights">GrantedRights</a>" : <i>[ String, ... ]</i>,
        "<a href="#rolename" title="RoleName">RoleName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::CustomRole
Properties:
    <a href="#disallowedrights" title="DisallowedRights">DisallowedRights</a>: <i>
      - String</i>
    <a href="#extendedrole" title="ExtendedRole">ExtendedRole</a>: <i>String</i>
    <a href="#grantedrights" title="GrantedRights">GrantedRights</a>: <i>
      - String</i>
    <a href="#rolename" title="RoleName">RoleName</a>: <i>String</i>
</pre>

## Properties

#### DisallowedRights

The rights this role cannot have. For allowed values please refer [User Right Prerequisites](https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedRole

The role from which this role has been derived. Allowed Values: "user", "observer", "stakeholder".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrantedRights

The rights granted to this role. For allowed values please refer [User Right Prerequisites](https://docs.opsgenie.com/docs/custom-user-role-api#section-user-right-prerequisites).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleName

Name of the custom role.

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

