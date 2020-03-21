# Terraform::AWS::KinesisFirehoseDeliveryStream OrcSerDe

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#blocksizebytes" title="BlockSizeBytes">BlockSizeBytes</a>" : <i>Double</i>,
    "<a href="#bloomfiltercolumns" title="BloomFilterColumns">BloomFilterColumns</a>" : <i>[ String, ... ]</i>,
    "<a href="#bloomfilterfalsepositiveprobability" title="BloomFilterFalsePositiveProbability">BloomFilterFalsePositiveProbability</a>" : <i>Double</i>,
    "<a href="#compression" title="Compression">Compression</a>" : <i>String</i>,
    "<a href="#dictionarykeythreshold" title="DictionaryKeyThreshold">DictionaryKeyThreshold</a>" : <i>Double</i>,
    "<a href="#enablepadding" title="EnablePadding">EnablePadding</a>" : <i>Boolean</i>,
    "<a href="#formatversion" title="FormatVersion">FormatVersion</a>" : <i>String</i>,
    "<a href="#paddingtolerance" title="PaddingTolerance">PaddingTolerance</a>" : <i>Double</i>,
    "<a href="#rowindexstride" title="RowIndexStride">RowIndexStride</a>" : <i>Double</i>,
    "<a href="#stripesizebytes" title="StripeSizeBytes">StripeSizeBytes</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#blocksizebytes" title="BlockSizeBytes">BlockSizeBytes</a>: <i>Double</i>
<a href="#bloomfiltercolumns" title="BloomFilterColumns">BloomFilterColumns</a>: <i>
      - String</i>
<a href="#bloomfilterfalsepositiveprobability" title="BloomFilterFalsePositiveProbability">BloomFilterFalsePositiveProbability</a>: <i>Double</i>
<a href="#compression" title="Compression">Compression</a>: <i>String</i>
<a href="#dictionarykeythreshold" title="DictionaryKeyThreshold">DictionaryKeyThreshold</a>: <i>Double</i>
<a href="#enablepadding" title="EnablePadding">EnablePadding</a>: <i>Boolean</i>
<a href="#formatversion" title="FormatVersion">FormatVersion</a>: <i>String</i>
<a href="#paddingtolerance" title="PaddingTolerance">PaddingTolerance</a>: <i>Double</i>
<a href="#rowindexstride" title="RowIndexStride">RowIndexStride</a>: <i>Double</i>
<a href="#stripesizebytes" title="StripeSizeBytes">StripeSizeBytes</a>: <i>Double</i>
</pre>

## Properties

#### BlockSizeBytes

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BloomFilterColumns

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BloomFilterFalsePositiveProbability

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compression

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DictionaryKeyThreshold

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePadding

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormatVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PaddingTolerance

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RowIndexStride

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StripeSizeBytes

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

