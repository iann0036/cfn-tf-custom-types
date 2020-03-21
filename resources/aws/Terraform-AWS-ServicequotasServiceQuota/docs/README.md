# Terraform::AWS::ServicequotasServiceQuota

CloudFormation equivalent of aws_servicequotas_service_quota

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ServicequotasServiceQuota",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#adjustable" title="Adjustable">Adjustable</a>" : <i>Boolean</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#defaultvalue" title="DefaultValue">DefaultValue</a>" : <i>Double</i>,
        "<a href="#quotacode" title="QuotaCode">QuotaCode</a>" : <i>String</i>,
        "<a href="#quotaname" title="QuotaName">QuotaName</a>" : <i>String</i>,
        "<a href="#requestid" title="RequestId">RequestId</a>" : <i>String</i>,
        "<a href="#requeststatus" title="RequestStatus">RequestStatus</a>" : <i>String</i>,
        "<a href="#servicecode" title="ServiceCode">ServiceCode</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ServicequotasServiceQuota
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#adjustable" title="Adjustable">Adjustable</a>: <i>Boolean</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#defaultvalue" title="DefaultValue">DefaultValue</a>: <i>Double</i>
    <a href="#quotacode" title="QuotaCode">QuotaCode</a>: <i>String</i>
    <a href="#quotaname" title="QuotaName">QuotaName</a>: <i>String</i>
    <a href="#requestid" title="RequestId">RequestId</a>: <i>String</i>
    <a href="#requeststatus" title="RequestStatus">RequestStatus</a>: <i>String</i>
    <a href="#servicecode" title="ServiceCode">ServiceCode</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>Double</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Adjustable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Adjustable

Returns the &lt;code&gt;Adjustable&lt;/code&gt; value.

#### Arn

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### DefaultValue

Returns the &lt;code&gt;DefaultValue&lt;/code&gt; value.

#### QuotaName

Returns the &lt;code&gt;QuotaName&lt;/code&gt; value.

#### RequestId

Returns the &lt;code&gt;RequestId&lt;/code&gt; value.

#### RequestStatus

Returns the &lt;code&gt;RequestStatus&lt;/code&gt; value.

#### ServiceName

Returns the &lt;code&gt;ServiceName&lt;/code&gt; value.

