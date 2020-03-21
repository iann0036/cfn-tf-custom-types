# Terraform::Docker::Service Privileges

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>" : <i>[ <a href="privileges-credentialspec.md">CredentialSpec</a>, ... ]</i>,
    "<a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>" : <i>[ <a href="privileges-selinuxcontext.md">SeLinuxContext</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#credentialspec" title="CredentialSpec">CredentialSpec</a>: <i>
      - <a href="privileges-credentialspec.md">CredentialSpec</a></i>
<a href="#selinuxcontext" title="SeLinuxContext">SeLinuxContext</a>: <i>
      - <a href="privileges-selinuxcontext.md">SeLinuxContext</a></i>
</pre>

## Properties

#### CredentialSpec

_Required_: No
_Type_: List of <a href="privileges-credentialspec.md">CredentialSpec</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxContext

_Required_: No
_Type_: List of <a href="privileges-selinuxcontext.md">SeLinuxContext</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

