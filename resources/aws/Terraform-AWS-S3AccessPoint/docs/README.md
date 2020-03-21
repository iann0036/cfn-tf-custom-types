# Terraform::AWS::S3AccessPoint

CloudFormation equivalent of aws_s3_access_point

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::S3AccessPoint",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#publicaccessblockconfiguration" title="PublicAccessBlockConfiguration">PublicAccessBlockConfiguration</a>" : <i>[ &lt;a href=&#34;publicaccessblockconfiguration.md&#34;&gt;PublicAccessBlockConfiguration&lt;/a&gt;, ... ]</i>,
        "<a href="#vpcconfiguration" title="VpcConfiguration">VpcConfiguration</a>" : <i>[ &lt;a href=&#34;vpcconfiguration.md&#34;&gt;VpcConfiguration&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::S3AccessPoint
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#publicaccessblockconfiguration" title="PublicAccessBlockConfiguration">PublicAccessBlockConfiguration</a>: <i>
      - &lt;a href=&#34;publicaccessblockconfiguration.md&#34;&gt;PublicAccessBlockConfiguration&lt;/a&gt;</i>
    <a href="#vpcconfiguration" title="VpcConfiguration">VpcConfiguration</a>: <i>
      - &lt;a href=&#34;vpcconfiguration.md&#34;&gt;VpcConfiguration&lt;/a&gt;</i>
</pre>

## Properties

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccessBlockConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;publicaccessblockconfiguration.md&#34;&gt;PublicAccessBlockConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfiguration

_Required_: No

_Type_: List of &lt;a href=&#34;vpcconfiguration.md&#34;&gt;VpcConfiguration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### DomainName

Returns the &lt;code&gt;DomainName&lt;/code&gt; value.

#### HasPublicAccessPolicy

Returns the &lt;code&gt;HasPublicAccessPolicy&lt;/code&gt; value.

#### NetworkOrigin

Returns the &lt;code&gt;NetworkOrigin&lt;/code&gt; value.

