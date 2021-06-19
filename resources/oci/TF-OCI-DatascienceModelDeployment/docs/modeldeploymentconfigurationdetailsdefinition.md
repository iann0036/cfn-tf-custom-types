# TF::OCI::DatascienceModelDeployment ModelDeploymentConfigurationDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>" : <i>String</i>,
    "<a href="#modelconfigurationdetails" title="ModelConfigurationDetails">ModelConfigurationDetails</a>" : <i>[ <a href="modelconfigurationdetailsdefinition.md">ModelConfigurationDetailsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#deploymenttype" title="DeploymentType">DeploymentType</a>: <i>String</i>
<a href="#modelconfigurationdetails" title="ModelConfigurationDetails">ModelConfigurationDetails</a>: <i>
      - <a href="modelconfigurationdetailsdefinition.md">ModelConfigurationDetailsDefinition</a></i>
</pre>

## Properties

#### DeploymentType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelConfigurationDetails

_Required_: No

_Type_: List of <a href="modelconfigurationdetailsdefinition.md">ModelConfigurationDetailsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

