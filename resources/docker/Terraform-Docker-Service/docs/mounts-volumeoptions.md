# Terraform::Docker::Service Mounts VolumeOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#drivername" title="DriverName">DriverName</a>" : <i>String</i>,
    "<a href="#driveroptions" title="DriverOptions">DriverOptions</a>" : <i>[ &lt;a href=&#34;mounts-volumeoptions-driveroptions.md&#34;&gt;DriverOptions&lt;/a&gt;, ... ]</i>,
    "<a href="#nocopy" title="NoCopy">NoCopy</a>" : <i>Boolean</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;mounts-volumeoptions-labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#drivername" title="DriverName">DriverName</a>: <i>String</i>
<a href="#driveroptions" title="DriverOptions">DriverOptions</a>: <i>
      - &lt;a href=&#34;mounts-volumeoptions-driveroptions.md&#34;&gt;DriverOptions&lt;/a&gt;</i>
<a href="#nocopy" title="NoCopy">NoCopy</a>: <i>Boolean</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;mounts-volumeoptions-labels.md&#34;&gt;Labels&lt;/a&gt;</i>
</pre>

## Properties

#### DriverName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DriverOptions

_Required_: No
_Type_: List of &lt;a href=&#34;mounts-volumeoptions-driveroptions.md&#34;&gt;DriverOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoCopy

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No
_Type_: List of &lt;a href=&#34;mounts-volumeoptions-labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

