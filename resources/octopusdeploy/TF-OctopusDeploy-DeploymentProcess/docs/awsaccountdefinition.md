# TF::OctopusDeploy::DeploymentProcess AwsAccountDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#useinstancerole" title="UseInstanceRole">UseInstanceRole</a>" : <i>Boolean</i>,
    "<a href="#variable" title="Variable">Variable</a>" : <i>String</i>,
    "<a href="#role" title="Role">Role</a>" : <i>[ <a href="roledefinition.md">RoleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#useinstancerole" title="UseInstanceRole">UseInstanceRole</a>: <i>Boolean</i>
<a href="#variable" title="Variable">Variable</a>: <i>String</i>
<a href="#role" title="Role">Role</a>: <i>
      - <a href="roledefinition.md">RoleDefinition</a></i>
</pre>

## Properties

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseInstanceRole

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Variable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: No

_Type_: List of <a href="roledefinition.md">RoleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

