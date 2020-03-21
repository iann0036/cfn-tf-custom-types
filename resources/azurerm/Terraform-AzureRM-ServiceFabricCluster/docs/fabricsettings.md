# Terraform::AzureRM::ServiceFabricCluster FabricSettings

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="fabricsettings-parameters.md">Parameters</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="fabricsettings-parameters.md">Parameters</a></i>
</pre>

## Properties

#### Name

The name of the Fabric Setting, such as `Security` or `Federation`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

A map containing settings for the specified Fabric Setting.

_Required_: No

_Type_: List of <a href="fabricsettings-parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

