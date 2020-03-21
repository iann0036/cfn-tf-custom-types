# Terraform::Skytap::Project

Provides a Skytap Project resource. Projects are an access permissions model used to share environments, 
templates, and assets with other users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Skytap::Project",
    "Properties" : {
        "<a href="#autoaddrolename" title="AutoAddRoleName">AutoAddRoleName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#showprojectmembers" title="ShowProjectMembers">ShowProjectMembers</a>" : <i>Boolean</i>,
        "<a href="#summary" title="Summary">Summary</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Skytap::Project
Properties:
    <a href="#autoaddrolename" title="AutoAddRoleName">AutoAddRoleName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#showprojectmembers" title="ShowProjectMembers">ShowProjectMembers</a>: <i>Boolean</i>
    <a href="#summary" title="Summary">Summary</a>: <i>String</i>
</pre>

## Properties

#### AutoAddRoleName

If this field is set to `viewer`, `participant`, `editor`, or `manager`, new users added to your Skytap account are automatically added to this project with the specified project role. Existing users aren’t affected by this setting. If the field is set to `null`, new users aren’t automatically added to the project. For additional details, see [Automatically adding new users to a project](https://help.skytap.com/csh-project-automatic-role.html).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

User-defined project name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShowProjectMembers

Determines whether projects members can view a list of other project members. False by default.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Summary

User-defined description of project.

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

