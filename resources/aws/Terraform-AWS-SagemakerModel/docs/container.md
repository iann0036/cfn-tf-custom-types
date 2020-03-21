# Terraform::AWS::SagemakerModel Container

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#containerhostname" title="ContainerHostname">ContainerHostname</a>" : <i>String</i>,
    "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="container-environment.md">Environment</a>, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#modeldataurl" title="ModelDataUrl">ModelDataUrl</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#containerhostname" title="ContainerHostname">ContainerHostname</a>: <i>String</i>
<a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="container-environment.md">Environment</a></i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#modeldataurl" title="ModelDataUrl">ModelDataUrl</a>: <i>String</i>
</pre>

## Properties

#### ContainerHostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of <a href="container-environment.md">Environment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelDataUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

