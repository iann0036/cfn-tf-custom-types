# TF::AWS::AmplifyBackendEnvironment

Provides an Amplify Backend Environment resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AmplifyBackendEnvironment",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#deploymentartifacts" title="DeploymentArtifacts">DeploymentArtifacts</a>" : <i>String</i>,
        "<a href="#environmentname" title="EnvironmentName">EnvironmentName</a>" : <i>String</i>,
        "<a href="#stackname" title="StackName">StackName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AmplifyBackendEnvironment
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#deploymentartifacts" title="DeploymentArtifacts">DeploymentArtifacts</a>: <i>String</i>
    <a href="#environmentname" title="EnvironmentName">EnvironmentName</a>: <i>String</i>
    <a href="#stackname" title="StackName">StackName</a>: <i>String</i>
</pre>

## Properties

#### AppId

The unique ID for an Amplify app.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeploymentArtifacts

The name of deployment artifacts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentName

The name for the backend environment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StackName

The AWS CloudFormation stack name of a backend environment.

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

