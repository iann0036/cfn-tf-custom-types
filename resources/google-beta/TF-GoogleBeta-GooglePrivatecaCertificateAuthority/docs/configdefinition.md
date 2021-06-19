# TF::GoogleBeta::GooglePrivatecaCertificateAuthority ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#reusableconfig" title="ReusableConfig">ReusableConfig</a>" : <i>[ <a href="reusableconfigdefinition.md">ReusableConfigDefinition</a>, ... ]</i>,
    "<a href="#subjectconfig" title="SubjectConfig">SubjectConfig</a>" : <i>[ <a href="subjectconfigdefinition.md">SubjectConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#reusableconfig" title="ReusableConfig">ReusableConfig</a>: <i>
      - <a href="reusableconfigdefinition.md">ReusableConfigDefinition</a></i>
<a href="#subjectconfig" title="SubjectConfig">SubjectConfig</a>: <i>
      - <a href="subjectconfigdefinition.md">SubjectConfigDefinition</a></i>
</pre>

## Properties

#### ReusableConfig

_Required_: No

_Type_: List of <a href="reusableconfigdefinition.md">ReusableConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectConfig

_Required_: No

_Type_: List of <a href="subjectconfigdefinition.md">SubjectConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

