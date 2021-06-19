# TF::Rancher2::PodSecurityPolicyTemplate SeLinuxDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#rule" title="Rule">Rule</a>" : <i>String</i>,
    "<a href="#selinuxoption" title="SeLinuxOption">SeLinuxOption</a>" : <i>[ <a href="selinuxoptiondefinition.md">SeLinuxOptionDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#rule" title="Rule">Rule</a>: <i>String</i>
<a href="#selinuxoption" title="SeLinuxOption">SeLinuxOption</a>: <i>
      - <a href="selinuxoptiondefinition.md">SeLinuxOptionDefinition</a></i>
</pre>

## Properties

#### Rule

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxOption

_Required_: No

_Type_: List of <a href="selinuxoptiondefinition.md">SeLinuxOptionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

