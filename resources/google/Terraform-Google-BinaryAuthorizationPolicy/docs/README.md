# Terraform::Google::BinaryAuthorizationPolicy

CloudFormation equivalent of google_binary_authorization_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::BinaryAuthorizationPolicy",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#globalpolicyevaluationmode" title="GlobalPolicyEvaluationMode">GlobalPolicyEvaluationMode</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#admissionwhitelistpatterns" title="AdmissionWhitelistPatterns">AdmissionWhitelistPatterns</a>" : <i>[ &lt;a href=&#34;admissionwhitelistpatterns.md&#34;&gt;AdmissionWhitelistPatterns&lt;/a&gt;, ... ]</i>,
        "<a href="#clusteradmissionrules" title="ClusterAdmissionRules">ClusterAdmissionRules</a>" : <i>[ &lt;a href=&#34;clusteradmissionrules.md&#34;&gt;ClusterAdmissionRules&lt;/a&gt;, ... ]</i>,
        "<a href="#defaultadmissionrule" title="DefaultAdmissionRule">DefaultAdmissionRule</a>" : <i>[ &lt;a href=&#34;defaultadmissionrule.md&#34;&gt;DefaultAdmissionRule&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::BinaryAuthorizationPolicy
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#globalpolicyevaluationmode" title="GlobalPolicyEvaluationMode">GlobalPolicyEvaluationMode</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#admissionwhitelistpatterns" title="AdmissionWhitelistPatterns">AdmissionWhitelistPatterns</a>: <i>
      - &lt;a href=&#34;admissionwhitelistpatterns.md&#34;&gt;AdmissionWhitelistPatterns&lt;/a&gt;</i>
    <a href="#clusteradmissionrules" title="ClusterAdmissionRules">ClusterAdmissionRules</a>: <i>
      - &lt;a href=&#34;clusteradmissionrules.md&#34;&gt;ClusterAdmissionRules&lt;/a&gt;</i>
    <a href="#defaultadmissionrule" title="DefaultAdmissionRule">DefaultAdmissionRule</a>: <i>
      - &lt;a href=&#34;defaultadmissionrule.md&#34;&gt;DefaultAdmissionRule&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalPolicyEvaluationMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdmissionWhitelistPatterns

_Required_: No

_Type_: List of &lt;a href=&#34;admissionwhitelistpatterns.md&#34;&gt;AdmissionWhitelistPatterns&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterAdmissionRules

_Required_: No

_Type_: List of &lt;a href=&#34;clusteradmissionrules.md&#34;&gt;ClusterAdmissionRules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultAdmissionRule

_Required_: No

_Type_: List of &lt;a href=&#34;defaultadmissionrule.md&#34;&gt;DefaultAdmissionRule&lt;/a&gt;

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

