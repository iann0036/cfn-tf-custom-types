# Terraform::Google::CloudRunService

CloudFormation equivalent of google_cloud_run_service

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::CloudRunService",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>[ &lt;a href=&#34;status.md&#34;&gt;Status&lt;/a&gt;, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#traffic" title="Traffic">Traffic</a>" : <i>[ &lt;a href=&#34;traffic.md&#34;&gt;Traffic&lt;/a&gt;, ... ]</i>,
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;, ... ]</i>,
        "<a href="#containers" title="Containers">Containers</a>" : <i>[ &lt;a href=&#34;containers.md&#34;&gt;Containers&lt;/a&gt;, ... ]</i>,
        "<a href="#env" title="Env">Env</a>" : <i>[ &lt;a href=&#34;env.md&#34;&gt;Env&lt;/a&gt;, ... ]</i>,
        "<a href="#envfrom" title="EnvFrom">EnvFrom</a>" : <i>[ &lt;a href=&#34;envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;, ... ]</i>,
        "<a href="#resources" title="Resources">Resources</a>" : <i>[ &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;, ... ]</i>,
        "<a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>" : <i>[ &lt;a href=&#34;configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;, ... ]</i>,
        "<a href="#secretref" title="SecretRef">SecretRef</a>" : <i>[ &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;, ... ]</i>,
        "<a href="#localobjectreference" title="LocalObjectReference">LocalObjectReference</a>" : <i>[ &lt;a href=&#34;localobjectreference.md&#34;&gt;LocalObjectReference&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::CloudRunService
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>
      - &lt;a href=&#34;status.md&#34;&gt;Status&lt;/a&gt;</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#template" title="Template">Template</a>: <i>
      - &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#traffic" title="Traffic">Traffic</a>: <i>
      - &lt;a href=&#34;traffic.md&#34;&gt;Traffic&lt;/a&gt;</i>
    <a href="#spec" title="Spec">Spec</a>: <i>
      - &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;</i>
    <a href="#containers" title="Containers">Containers</a>: <i>
      - &lt;a href=&#34;containers.md&#34;&gt;Containers&lt;/a&gt;</i>
    <a href="#env" title="Env">Env</a>: <i>
      - &lt;a href=&#34;env.md&#34;&gt;Env&lt;/a&gt;</i>
    <a href="#envfrom" title="EnvFrom">EnvFrom</a>: <i>
      - &lt;a href=&#34;envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;</i>
    <a href="#resources" title="Resources">Resources</a>: <i>
      - &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;</i>
    <a href="#configmapref" title="ConfigMapRef">ConfigMapRef</a>: <i>
      - &lt;a href=&#34;configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;</i>
    <a href="#secretref" title="SecretRef">SecretRef</a>: <i>
      - &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;</i>
    <a href="#localobjectreference" title="LocalObjectReference">LocalObjectReference</a>: <i>
      - &lt;a href=&#34;localobjectreference.md&#34;&gt;LocalObjectReference&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: Yes

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

#### Status

_Required_: No

_Type_: List of &lt;a href=&#34;status.md&#34;&gt;Status&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of &lt;a href=&#34;template.md&#34;&gt;Template&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Traffic

_Required_: No

_Type_: List of &lt;a href=&#34;traffic.md&#34;&gt;Traffic&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Spec

_Required_: No

_Type_: List of &lt;a href=&#34;spec.md&#34;&gt;Spec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Containers

_Required_: No

_Type_: List of &lt;a href=&#34;containers.md&#34;&gt;Containers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Env

_Required_: No

_Type_: List of &lt;a href=&#34;env.md&#34;&gt;Env&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvFrom

_Required_: No

_Type_: List of &lt;a href=&#34;envfrom.md&#34;&gt;EnvFrom&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: No

_Type_: List of &lt;a href=&#34;resources.md&#34;&gt;Resources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMapRef

_Required_: No

_Type_: List of &lt;a href=&#34;configmapref.md&#34;&gt;ConfigMapRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretRef

_Required_: No

_Type_: List of &lt;a href=&#34;secretref.md&#34;&gt;SecretRef&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalObjectReference

_Required_: No

_Type_: List of &lt;a href=&#34;localobjectreference.md&#34;&gt;LocalObjectReference&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

