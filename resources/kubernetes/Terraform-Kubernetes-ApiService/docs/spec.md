# Terraform::Kubernetes::ApiService Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cabundle" title="CaBundle">CaBundle</a>" : <i>String</i>,
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#grouppriorityminimum" title="GroupPriorityMinimum">GroupPriorityMinimum</a>" : <i>Double</i>,
    "<a href="#insecureskiptlsverify" title="InsecureSkipTlsVerify">InsecureSkipTlsVerify</a>" : <i>Boolean</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#versionpriority" title="VersionPriority">VersionPriority</a>" : <i>Double</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ &lt;a href=&#34;spec-service.md&#34;&gt;Service&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cabundle" title="CaBundle">CaBundle</a>: <i>String</i>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#grouppriorityminimum" title="GroupPriorityMinimum">GroupPriorityMinimum</a>: <i>Double</i>
<a href="#insecureskiptlsverify" title="InsecureSkipTlsVerify">InsecureSkipTlsVerify</a>: <i>Boolean</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#versionpriority" title="VersionPriority">VersionPriority</a>: <i>Double</i>
<a href="#service" title="Service">Service</a>: <i>
      - &lt;a href=&#34;spec-service.md&#34;&gt;Service&lt;/a&gt;</i>
</pre>

## Properties

#### CaBundle

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupPriorityMinimum

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsecureSkipTlsVerify

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionPriority

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No
_Type_: List of &lt;a href=&#34;spec-service.md&#34;&gt;Service&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

