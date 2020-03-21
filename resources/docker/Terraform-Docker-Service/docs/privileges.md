# Terraform::Docker::Service Privileges

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>" : <i>[ &lt;a href=&#34;privileges-credentialspec.md&#34;&gt;CredentialSpec&lt;/a&gt;, ... ]</i>,
    "<a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>" : <i>[ &lt;a href=&#34;privileges-selinuxcontext.md&#34;&gt;SeLinuxContext&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>: <i>
      - &lt;a href=&#34;privileges-credentialspec.md&#34;&gt;CredentialSpec&lt;/a&gt;</i>
<a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>: <i>
      - &lt;a href=&#34;privileges-selinuxcontext.md&#34;&gt;SeLinuxContext&lt;/a&gt;</i>
</pre>

## Properties

#### CredentialSpec

_Required_: No
_Type_: List of &lt;a href=&#34;privileges-credentialspec.md&#34;&gt;CredentialSpec&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxContext

_Required_: No
_Type_: List of &lt;a href=&#34;privileges-selinuxcontext.md&#34;&gt;SeLinuxContext&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

