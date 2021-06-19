# TF::OktaASA::AssignGroup

The oktaasa_assign_group resource assigns control access levels in group definitions in Okta's ASA.  In order to give access to project, you need to assign an Okta group to a project. Use "server_access" and "server_admin" parameters to control access level.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OktaASA::AssignGroup",
    "Properties" : {
        "<a href="#createservergroup" title="CreateServerGroup">CreateServerGroup</a>" : <i>Boolean</i>,
        "<a href="#groupname" title="GroupName">GroupName</a>" : <i>String</i>,
        "<a href="#projectname" title="ProjectName">ProjectName</a>" : <i>String</i>,
        "<a href="#serveraccess" title="ServerAccess">ServerAccess</a>" : <i>Boolean</i>,
        "<a href="#serveradmin" title="ServerAdmin">ServerAdmin</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OktaASA::AssignGroup
Properties:
    <a href="#createservergroup" title="CreateServerGroup">CreateServerGroup</a>: <i>Boolean</i>
    <a href="#groupname" title="GroupName">GroupName</a>: <i>String</i>
    <a href="#projectname" title="ProjectName">ProjectName</a>: <i>String</i>
    <a href="#serveraccess" title="ServerAccess">ServerAccess</a>: <i>Boolean</i>
    <a href="#serveradmin" title="ServerAdmin">ServerAdmin</a>: <i>Boolean</i>
</pre>

## Properties

#### CreateServerGroup

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAdmin

_Required_: No

_Type_: Boolean

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

