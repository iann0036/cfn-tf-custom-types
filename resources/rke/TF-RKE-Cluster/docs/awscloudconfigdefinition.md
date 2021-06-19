# TF::RKE::Cluster AwsCloudConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#global" title="Global">Global</a>" : <i>[ <a href="globaldefinition.md">GlobalDefinition</a>, ... ]</i>,
    "<a href="#serviceoverride" title="ServiceOverride">ServiceOverride</a>" : <i>[ <a href="serviceoverridedefinition.md">ServiceOverrideDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#global" title="Global">Global</a>: <i>
      - <a href="globaldefinition.md">GlobalDefinition</a></i>
<a href="#serviceoverride" title="ServiceOverride">ServiceOverride</a>: <i>
      - <a href="serviceoverridedefinition.md">ServiceOverrideDefinition</a></i>
</pre>

## Properties

#### Global

_Required_: No

_Type_: List of <a href="globaldefinition.md">GlobalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceOverride

_Required_: No

_Type_: List of <a href="serviceoverridedefinition.md">ServiceOverrideDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

