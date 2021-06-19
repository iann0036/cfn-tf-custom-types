# TF::AWS::CodebuildProject BuildBatchConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#combineartifacts" title="CombineArtifacts">CombineArtifacts</a>" : <i>Boolean</i>,
    "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
    "<a href="#timeoutinmins" title="TimeoutInMins">TimeoutInMins</a>" : <i>Double</i>,
    "<a href="#restrictions" title="Restrictions">Restrictions</a>" : <i>[ <a href="restrictionsdefinition.md">RestrictionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#combineartifacts" title="CombineArtifacts">CombineArtifacts</a>: <i>Boolean</i>
<a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
<a href="#timeoutinmins" title="TimeoutInMins">TimeoutInMins</a>: <i>Double</i>
<a href="#restrictions" title="Restrictions">Restrictions</a>: <i>
      - <a href="restrictionsdefinition.md">RestrictionsDefinition</a></i>
</pre>

## Properties

#### CombineArtifacts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutInMins

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Restrictions

_Required_: No

_Type_: List of <a href="restrictionsdefinition.md">RestrictionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

