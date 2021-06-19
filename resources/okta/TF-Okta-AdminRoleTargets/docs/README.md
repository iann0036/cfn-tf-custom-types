# TF::Okta::AdminRoleTargets

Manages targets for administrator roles.

This resource allows you to define permissions for admin roles into a smaller subset of Groups or Apps within your org.
You can define admin roles to target Groups, Applications, and Application Instances.

```
Note 1: you have to assign a role to a user before creating this resource.

Note 2: You can target a mixture of both App and App Instance targets, but can't assign permissions to manage all 
        instances of an App and then a subset of that same App. For example, you can't specify that an admin has access 
        to manage all instances of a Salesforce app and then also specific configurations of the Salesforce app.
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Okta::AdminRoleTargets",
    "Properties" : {
        "<a href="#apps" title="Apps">Apps</a>" : <i>[ String, ... ]</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#roletype" title="RoleType">RoleType</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Okta::AdminRoleTargets
Properties:
    <a href="#apps" title="Apps">Apps</a>: <i>
      - String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#roletype" title="RoleType">RoleType</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
</pre>

## Properties

#### Apps

List of app names (name represents set of app instances) or a combination of app name and app instance ID (like 'salesforce' or 'facebook.0oapsqQ6dv19pqyEo0g3').

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleType

Name of the role associated with the user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

ID of the user.

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

#### RoleId

Returns the <code>RoleId</code> value.

