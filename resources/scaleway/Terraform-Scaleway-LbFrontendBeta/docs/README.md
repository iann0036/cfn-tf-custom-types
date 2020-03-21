# Terraform::Scaleway::LbFrontendBeta

CloudFormation equivalent of scaleway_lb_frontend_beta

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::LbFrontendBeta",
    "Properties" : {
        "<a href="#backendid" title="BackendId">BackendId</a>" : <i>String</i>,
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#inboundport" title="InboundPort">InboundPort</a>" : <i>Double</i>,
        "<a href="#lbid" title="LbId">LbId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#timeoutclient" title="TimeoutClient">TimeoutClient</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>[ &lt;a href=&#34;acl.md&#34;&gt;Acl&lt;/a&gt;, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#match" title="Match">Match</a>" : <i>[ &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::LbFrontendBeta
Properties:
    <a href="#backendid" title="BackendId">BackendId</a>: <i>String</i>
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#inboundport" title="InboundPort">InboundPort</a>: <i>Double</i>
    <a href="#lbid" title="LbId">LbId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#timeoutclient" title="TimeoutClient">TimeoutClient</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>
      - &lt;a href=&#34;acl.md&#34;&gt;Acl&lt;/a&gt;</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#match" title="Match">Match</a>: <i>
      - &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;</i>
</pre>

## Properties

#### BackendId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundPort

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LbId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutClient

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

_Required_: No

_Type_: List of &lt;a href=&#34;acl.md&#34;&gt;Acl&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No

_Type_: List of &lt;a href=&#34;match.md&#34;&gt;Match&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

