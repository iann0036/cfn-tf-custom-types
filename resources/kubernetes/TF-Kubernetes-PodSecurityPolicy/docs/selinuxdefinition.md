# TF::Kubernetes::PodSecurityPolicy SeLinuxDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rule" title="Rule">Rule</a>" : <i>String</i>,
    "<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>" : <i>[ <a href="selinuxoptionsdefinition.md">SeLinuxOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rule" title="Rule">Rule</a>: <i>String</i>
<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>: <i>
      - <a href="selinuxoptionsdefinition.md">SeLinuxOptionsDefinition</a></i>
</pre>

## Properties

#### Rule

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxOptions

_Required_: No

_Type_: List of <a href="selinuxoptionsdefinition.md">SeLinuxOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

