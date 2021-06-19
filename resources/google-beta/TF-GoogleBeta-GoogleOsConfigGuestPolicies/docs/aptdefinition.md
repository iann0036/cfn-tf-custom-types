# TF::GoogleBeta::GoogleOsConfigGuestPolicies AptDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#archivetype" title="ArchiveType">ArchiveType</a>" : <i>String</i>,
    "<a href="#components" title="Components">Components</a>" : <i>[ String, ... ]</i>,
    "<a href="#distribution" title="Distribution">Distribution</a>" : <i>String</i>,
    "<a href="#gpgkey" title="GpgKey">GpgKey</a>" : <i>String</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#archivetype" title="ArchiveType">ArchiveType</a>: <i>String</i>
<a href="#components" title="Components">Components</a>: <i>
      - String</i>
<a href="#distribution" title="Distribution">Distribution</a>: <i>String</i>
<a href="#gpgkey" title="GpgKey">GpgKey</a>: <i>String</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
</pre>

## Properties

#### ArchiveType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Components

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distribution

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GpgKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

