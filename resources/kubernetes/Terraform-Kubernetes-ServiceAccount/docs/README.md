# Terraform::Kubernetes::ServiceAccount

CloudFormation equivalent of kubernetes_service_account

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::ServiceAccount",
    "Properties" : {
        "<a href="#automountserviceaccounttoken" title="AutomountServiceAccountToken">AutomountServiceAccountToken</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#imagepullsecret" title="ImagePullSecret">ImagePullSecret</a>" : <i>[ &lt;a href=&#34;imagepullsecret.md&#34;&gt;ImagePullSecret&lt;/a&gt;, ... ]</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;, ... ]</i>,
        "<a href="#secret" title="Secret">Secret</a>" : <i>[ &lt;a href=&#34;secret.md&#34;&gt;Secret&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::ServiceAccount
Properties:
    <a href="#automountserviceaccounttoken" title="AutomountServiceAccountToken">AutomountServiceAccountToken</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#imagepullsecret" title="ImagePullSecret">ImagePullSecret</a>: <i>
      - &lt;a href=&#34;imagepullsecret.md&#34;&gt;ImagePullSecret&lt;/a&gt;</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;</i>
    <a href="#secret" title="Secret">Secret</a>: <i>
      - &lt;a href=&#34;secret.md&#34;&gt;Secret&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### AutomountServiceAccountToken

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullSecret

_Required_: No

_Type_: List of &lt;a href=&#34;imagepullsecret.md&#34;&gt;ImagePullSecret&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of &lt;a href=&#34;metadata.md&#34;&gt;Metadata&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secret

_Required_: No

_Type_: List of &lt;a href=&#34;secret.md&#34;&gt;Secret&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DefaultSecretName

Returns the &lt;code&gt;DefaultSecretName&lt;/code&gt; value.

