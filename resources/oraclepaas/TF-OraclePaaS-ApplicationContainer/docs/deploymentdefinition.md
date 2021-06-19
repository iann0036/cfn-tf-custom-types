# TF::OraclePaaS::ApplicationContainer DeploymentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environmentdefinition.md">EnvironmentDefinition</a>, ... ]</i>,
    "<a href="#instances" title="Instances">Instances</a>" : <i>Double</i>,
    "<a href="#javasystemproperties" title="JavaSystemProperties">JavaSystemProperties</a>" : <i>[ <a href="javasystempropertiesdefinition.md">JavaSystemPropertiesDefinition</a>, ... ]</i>,
    "<a href="#memory" title="Memory">Memory</a>" : <i>String</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
    "<a href="#secureenvironment" title="SecureEnvironment">SecureEnvironment</a>" : <i>[ String, ... ]</i>,
    "<a href="#services" title="Services">Services</a>" : <i>[ <a href="servicesdefinition.md">ServicesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environmentdefinition.md">EnvironmentDefinition</a></i>
<a href="#instances" title="Instances">Instances</a>: <i>Double</i>
<a href="#javasystemproperties" title="JavaSystemProperties">JavaSystemProperties</a>: <i>
      - <a href="javasystempropertiesdefinition.md">JavaSystemPropertiesDefinition</a></i>
<a href="#memory" title="Memory">Memory</a>: <i>String</i>
<a href="#notes" title="Notes">Notes</a>: <i>String</i>
<a href="#secureenvironment" title="SecureEnvironment">SecureEnvironment</a>: <i>
      - String</i>
<a href="#services" title="Services">Services</a>: <i>
      - <a href="servicesdefinition.md">ServicesDefinition</a></i>
</pre>

## Properties

#### Environment

_Required_: No

_Type_: List of <a href="environmentdefinition.md">EnvironmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JavaSystemProperties

_Required_: No

_Type_: List of <a href="javasystempropertiesdefinition.md">JavaSystemPropertiesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Memory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecureEnvironment

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="servicesdefinition.md">ServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

