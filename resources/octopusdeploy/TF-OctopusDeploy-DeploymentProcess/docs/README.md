# TF::OctopusDeploy::DeploymentProcess

CloudFormation equivalent of octopusdeploy_deployment_process

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OctopusDeploy::DeploymentProcess",
    "Properties" : {
        "<a href="#lastsnapshotid" title="LastSnapshotId">LastSnapshotId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#spaceid" title="SpaceId">SpaceId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#step" title="Step">Step</a>" : <i>[ <a href="stepdefinition.md">StepDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OctopusDeploy::DeploymentProcess
Properties:
    <a href="#lastsnapshotid" title="LastSnapshotId">LastSnapshotId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#spaceid" title="SpaceId">SpaceId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#step" title="Step">Step</a>: <i>
      - <a href="stepdefinition.md">StepDefinition</a></i>
</pre>

## Properties

#### LastSnapshotId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Step

_Required_: No

_Type_: List of <a href="stepdefinition.md">StepDefinition</a>

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

