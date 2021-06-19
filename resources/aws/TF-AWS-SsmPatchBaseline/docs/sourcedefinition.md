# TF::AWS::SsmPatchBaseline SourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configuration" title="Configuration">Configuration</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#products" title="Products">Products</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configuration" title="Configuration">Configuration</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#products" title="Products">Products</a>: <i>
      - String</i>
</pre>

## Properties

#### Configuration

The value of the yum repo configuration. For information about other options available for your yum repository configuration, see the [`dnf.conf` documentation](https://man7.org/linux/man-pages/man5/dnf.conf.5.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name specified to identify the patch source.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Products

The specific operating system versions a patch repository applies to, such as `"Ubuntu16.04"`, `"AmazonLinux2016.09"`, `"RedhatEnterpriseLinux7.2"` or `"Suse12.7"`. For lists of supported product values, see [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html).

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

