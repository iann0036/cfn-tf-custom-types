# TF::OctopusDeploy::ProjectDeploymentTargetTrigger

CloudFormation equivalent of octopusdeploy_project_deployment_target_trigger

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OctopusDeploy::ProjectDeploymentTargetTrigger",
    "Properties" : {
        "<a href="#environmentids" title="EnvironmentIds">EnvironmentIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#eventcategories" title="EventCategories">EventCategories</a>" : <i>[ String, ... ]</i>,
        "<a href="#eventgroups" title="EventGroups">EventGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#roles" title="Roles">Roles</a>" : <i>[ String, ... ]</i>,
        "<a href="#shouldredeploy" title="ShouldRedeploy">ShouldRedeploy</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OctopusDeploy::ProjectDeploymentTargetTrigger
Properties:
    <a href="#environmentids" title="EnvironmentIds">EnvironmentIds</a>: <i>
      - String</i>
    <a href="#eventcategories" title="EventCategories">EventCategories</a>: <i>
      - String</i>
    <a href="#eventgroups" title="EventGroups">EventGroups</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#roles" title="Roles">Roles</a>: <i>
      - String</i>
    <a href="#shouldredeploy" title="ShouldRedeploy">ShouldRedeploy</a>: <i>Boolean</i>
</pre>

## Properties

#### EnvironmentIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventCategories

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShouldRedeploy

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

