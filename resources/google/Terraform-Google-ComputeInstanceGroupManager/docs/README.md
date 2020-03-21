# Terraform::Google::ComputeInstanceGroupManager

CloudFormation equivalent of google_compute_instance_group_manager

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeInstanceGroupManager",
    "Properties" : {
        "<a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#targetpools" title="TargetPools">TargetPools</a>" : <i>[ String, ... ]</i>,
        "<a href="#targetsize" title="TargetSize">TargetSize</a>" : <i>[ &lt;a href=&#34;targetsize.md&#34;&gt;TargetSize&lt;/a&gt;, ... ]</i>,
        "<a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>" : <i>Boolean</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#autohealingpolicies" title="AutoHealingPolicies">AutoHealingPolicies</a>" : <i>[ &lt;a href=&#34;autohealingpolicies.md&#34;&gt;AutoHealingPolicies&lt;/a&gt;, ... ]</i>,
        "<a href="#namedport" title="NamedPort">NamedPort</a>" : <i>[ &lt;a href=&#34;namedport.md&#34;&gt;NamedPort&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>" : <i>[ &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>[ &lt;a href=&#34;version.md&#34;&gt;Version&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeInstanceGroupManager
Properties:
    <a href="#baseinstancename" title="BaseInstanceName">BaseInstanceName</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#instancetemplate" title="InstanceTemplate">InstanceTemplate</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#targetpools" title="TargetPools">TargetPools</a>: <i>
      - String</i>
    <a href="#targetsize" title="TargetSize">TargetSize</a>: <i>
      - &lt;a href=&#34;targetsize.md&#34;&gt;TargetSize&lt;/a&gt;</i>
    <a href="#waitforinstances" title="WaitForInstances">WaitForInstances</a>: <i>Boolean</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#autohealingpolicies" title="AutoHealingPolicies">AutoHealingPolicies</a>: <i>
      - &lt;a href=&#34;autohealingpolicies.md&#34;&gt;AutoHealingPolicies&lt;/a&gt;</i>
    <a href="#namedport" title="NamedPort">NamedPort</a>: <i>
      - &lt;a href=&#34;namedport.md&#34;&gt;NamedPort&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#updatepolicy" title="UpdatePolicy">UpdatePolicy</a>: <i>
      - &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;</i>
    <a href="#version" title="Version">Version</a>: <i>
      - &lt;a href=&#34;version.md&#34;&gt;Version&lt;/a&gt;</i>
</pre>

## Properties

#### BaseInstanceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPools

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetSize

_Required_: No

_Type_: List of &lt;a href=&#34;targetsize.md&#34;&gt;TargetSize&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForInstances

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoHealingPolicies

_Required_: No

_Type_: List of &lt;a href=&#34;autohealingpolicies.md&#34;&gt;AutoHealingPolicies&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamedPort

_Required_: No

_Type_: List of &lt;a href=&#34;namedport.md&#34;&gt;NamedPort&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdatePolicy

_Required_: No

_Type_: List of &lt;a href=&#34;updatepolicy.md&#34;&gt;UpdatePolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: List of &lt;a href=&#34;version.md&#34;&gt;Version&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Fingerprint

Returns the &lt;code&gt;Fingerprint&lt;/code&gt; value.

#### InstanceGroup

Returns the &lt;code&gt;InstanceGroup&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

#### UpdateStrategy

Returns the &lt;code&gt;UpdateStrategy&lt;/code&gt; value.

