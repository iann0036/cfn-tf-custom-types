# Terraform::Google::DataprocJob PysparkConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#archiveuris" title="ArchiveUris">ArchiveUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#args" title="Args">Args</a>" : <i>[ String, ... ]</i>,
    "<a href="#fileuris" title="FileUris">FileUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#jarfileuris" title="JarFileUris">JarFileUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#mainpythonfileuri" title="MainPythonFileUri">MainPythonFileUri</a>" : <i>String</i>,
    "<a href="#properties" title="Properties">Properties</a>" : <i>[ &lt;a href=&#34;pysparkconfig-properties.md&#34;&gt;Properties&lt;/a&gt;, ... ]</i>,
    "<a href="#pythonfileuris" title="PythonFileUris">PythonFileUris</a>" : <i>[ String, ... ]</i>,
    "<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>" : <i>[ &lt;a href=&#34;pysparkconfig-loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#archiveuris" title="ArchiveUris">ArchiveUris</a>: <i>
      - String</i>
<a href="#args" title="Args">Args</a>: <i>
      - String</i>
<a href="#fileuris" title="FileUris">FileUris</a>: <i>
      - String</i>
<a href="#jarfileuris" title="JarFileUris">JarFileUris</a>: <i>
      - String</i>
<a href="#mainpythonfileuri" title="MainPythonFileUri">MainPythonFileUri</a>: <i>String</i>
<a href="#properties" title="Properties">Properties</a>: <i>
      - &lt;a href=&#34;pysparkconfig-properties.md&#34;&gt;Properties&lt;/a&gt;</i>
<a href="#pythonfileuris" title="PythonFileUris">PythonFileUris</a>: <i>
      - String</i>
<a href="#loggingconfig" title="LoggingConfig">LoggingConfig</a>: <i>
      - &lt;a href=&#34;pysparkconfig-loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;</i>
</pre>

## Properties

#### ArchiveUris

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Args

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileUris

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JarFileUris

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MainPythonFileUri

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Properties

_Required_: No
_Type_: List of &lt;a href=&#34;pysparkconfig-properties.md&#34;&gt;Properties&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PythonFileUris

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingConfig

_Required_: No
_Type_: List of &lt;a href=&#34;pysparkconfig-loggingconfig.md&#34;&gt;LoggingConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

